"""Datascrapter for UNC opprotuites board"""
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

URL = "https://our.unc.edu/find/opportunities/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

h1_elements = soup.find_all("h1")
date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
date_elements = soup.find_all("div", class_="col-md-10")

headings_list = []

for h1 in h1_elements:
    cleaned_text_title = h1.text.strip()
    headings_list.append(cleaned_text_title)

date_list = []

for date_element in date_elements:
    text_content = date_element.text.strip()
    if date_pattern.match(text_content):
        date_list.append(text_content)

date_list_post = []
date_list_close = []

for i in range(len(date_list)):
    if i % 2 == 1:
        everyother = date_list[i]
        date_list_close.append(everyother)
    else:
        everyother = date_list[i]
        date_list_post.append(everyother)

result_list = []

for i in range(len(date_elements)):
    paragraphs = date_elements[i].find_all('p')
    
    div_row_result = []
    
    for paragraph in paragraphs:
        task = paragraph.text.strip()
        div_row_result.append(task)
    
    result_list.append(div_row_result)

comp_list = []

for i in range(len(result_list)):
    if len(result_list[i]) > 0:
        comp_list.append(result_list[i])


URL2 = "https://www.blog.dailydoseofds.com/p/75-key-terms-that-all-data-scientists"
page_words = requests.get(URL2)
soup2 = BeautifulSoup(page_words.content, "html.parser")

words_elements = soup2.find_all('strong')

buzz_unfliterd = []
for i in words_elements:
    cleaned_words = ''.join(char for char in i.text if char.isalnum() or char.isspace())
    buzz_unfliterd.extend(cleaned_words.split())

buzz_list = []
uselesswords = ["the", "is", "of", "and", "a", "in", "that", "it", 'this', 'what']
for i in range(len(buzz_unfliterd)):
    current_word = str(buzz_unfliterd[i]).lower()
    if current_word not in uselesswords:
        buzz_list.append(current_word)

fit_array = []
for i in range(len(comp_list)):
    fit_number = 0
    split_list = str(comp_list[i]).lower().split()
    for j in range(len(split_list)):
        for k in range(len(buzz_list)):
            if split_list[j] == buzz_list[k]:
                fit_number += 1
    fit_array.append(fit_number)

libray = {'Title': headings_list[2:], 'Post Date': date_list_post, 'End Date': date_list_close, 'Fit': fit_array}
df = pd.DataFrame(data=libray)


print(df)