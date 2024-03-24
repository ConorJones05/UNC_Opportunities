import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

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
    return list_of_links[:-1], no_non_dep

url_list, major_abrv = findURLS()[0], findURLS()[1]


def find_all_elements(url):
    page2 = requests.get(url)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    courseblocks = soup2.find_all('div', class_='courseblock')
    
    if not courseblocks:  # If no course blocks are found, return empty lists
        return [], []

    codes_array = []
    name_array = []
    dec_array = []
    pre_array_basic = []
    ideas_in_action = []
    making_connections = []

    for block in range(len(courseblocks)):
        course_code = courseblocks[block].find(class_="text detail-code margin--tiny text--semibold text--big")
        codes_array.append(course_code.get_text(strip=True)[:-1])

        # course_name = courseblocks[block].find(class_="text detail-title margin--tiny text--semibold text--big")
        # name_array.append(course_name.get_text(strip=True)[:-1])

        # course_dec = courseblocks[block].find(class_="courseblockextra")
        # if course_dec:
        #     dec_array.append(course_dec.get_text(strip=False).lower())
        # else: 
        #     dec_array.append(None)

        course_pre_1 = courseblocks[block].find_all(class_="text detail-requisites margin--default")
        pre_small_array = []

        if course_pre_1:
            for element in course_pre_1:
                course_pre = element.find_all('a', {'title': True})
                for a_tag in course_pre:
                    pre_small_array.append(a_tag.get_text(strip=True).replace('\xa0', ' '))
                pre_array_basic.append(pre_small_array)
        else:
            pre_array_basic.append(None)

        # ideas_cur = courseblocks[block].find(class_="text detail-idea_action margin--default")
        # if ideas_cur:
        #     ideas_in_action.append(ideas_cur.get_text(strip=True)[:-1])
        # else:
        #     ideas_in_action.append(None)
        
        # connections_cur = courseblocks[block].find(class_="text detail-idea_action margin--default")
        # if connections_cur:
        #     making_connections.append(connections_cur.get_text(strip=True)[:-1])
        # else:
        #     making_connections.append(None)
    
    for i in pre_array_basic:
            if i is not None:
                for j in range(len(i)):
                    if i[j] is not None and len(i[j]) < 5:
                        i[j] = i[j-1][0:4] + ' ' + i[j]

    return codes_array, pre_array_basic


for i, url in enumerate(url_list):
    data = find_all_elements(url)
    max_prereqs = max(((len(prereqs) if prereqs is not None else 0) for prereqs in data[1]), default=0)

    rows = []
    for course_code, prereqs in zip(data[0], data[1]):
        row_dict = {'Course Code': course_code}
        if prereqs is not None:
            for j, prereq in enumerate(prereqs):
                row_dict[f'Prereq_{j+1}'] = prereq
            for j in range(len(prereqs), max_prereqs):
                row_dict[f'Prereq_{j+1}'] = None
        else:
            for j in range(1, max_prereqs + 1):
                row_dict[f'Prereq_{j}'] = None
        rows.append(row_dict)
    output_directory = "/Users/conor/conorjones-github/ConorJonesProjects/Vertuvisor/making_classes_list/classes_folder"
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(output_directory, f'Class_{major_abrv[i]}.csv'), index=False)
    print(f'File {major_abrv[i]} has been created')
    print(f'Program is {int(i/len(url_list)*100)}% Complete')
print('')
print('')
print("Program has finished running ")
