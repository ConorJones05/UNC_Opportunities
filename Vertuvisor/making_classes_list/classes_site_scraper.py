import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def findURLS():
    URL = "https://catalog.unc.edu/courses/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    parentheses_text = soup.find_all(text=re.compile(r'\((.*?)\)'))
    major_abrv = []
    for text in parentheses_text:
        match = re.search(r'\((.*?)\)', text)
        if match:
            major_abrv.append(match.group(1))
    no_non_dep = []
    for i in major_abrv:
        if len(i) < 6:
            no_non_dep.append(i)
    list_of_links = ['https://catalog.unc.edu/courses/' + ls.lower() + '/' for ls in no_non_dep]
    return list_of_links

url_list = ['https://catalog.unc.edu/courses/stor/']

def find_all_elements():
    for url in url_list:
        page2 = requests.get(url)
        soup2 = BeautifulSoup(page2.content, "html.parser")
        courseblocks = soup2.find_all('div', class_='courseblock')
        codes_array = []
        name_array = []
        dec_array = []
        pre_array_basic = []

        for block in range(len(courseblocks)):
            course_code = courseblocks[block].find(class_="text detail-code margin--tiny text--semibold text--big")
            codes_array.append(course_code.get_text(strip=True)[:-1])

            course_name = courseblocks[block].find(class_="text detail-title margin--tiny text--semibold text--big")
            name_array.append(course_name.get_text(strip=True)[:-1])

            course_dec = courseblocks[block].find(class_="courseblockextra")
            if course_dec:
                dec_array.append(course_dec.get_text(strip=False).lower())
            else: 
                dec_array.append(None)

            course_pre_1 = courseblocks[block].find_all(class_="text detail-requisites margin--default")
            pre_small_array = []

            for element in course_pre_1:
                course_pre = element.find_all('a', {'title': True})
                if course_pre:
                    for a_tag in course_pre:
                        pre_small_array.append(a_tag.get_text(strip=True).replace('\xa0', ' '))
                    pre_array_basic.append(pre_small_array)
                else:
                    pre_array_basic.append(None)

    return pre_array_basic 

def dict_builder():
    for i in find_all_elements():
        return i
    
print(len(find_all_elements()))



