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
        for block in courseblocks:
            course_code = soup2.find_all(class_="text detail-code margin--tiny text--semibold text--big")
            codes_array = []
            for clean_codes in course_code:
                cleaned_codes = clean_codes.get_text(strip=True)[:-1]
                codes_array.append(cleaned_codes)
            course_name = soup2.find_all(class_="text detail-title margin--tiny text--semibold text--big")
            name_array = []
            for clean_titles in course_name:
                cleaned_titles = clean_titles.get_text(strip=True)[:-1]
                name_array.append(cleaned_titles)
            course_dec = soup2.find_all(class_="courseblockextra")
            dec_array = []
            for clean_dec in course_dec:
                cleaned_codes = clean_dec.get_text(strip=True)[:-1].lower()
                dec_array.append(cleaned_codes)
            course_pre = soup2.find_all(class_="text detail-requisites margin--default")
            pre_array_basic = []
            for pre in course_pre:
                pre_clean = pre.get_text(strip=True)[:-1]
                pre_array_basic.append(pre_clean)
    return codes_array, name_array, dec_array, pre_array_basic


#def node_builder(pre_array_basic):
            

    




