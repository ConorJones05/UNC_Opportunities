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