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

URL2 = "https://www.blog.dailydoseofds.com/p/75-key-terms-that-all-data-scientists"
page_words = requests.get(URL2)
soup2 = BeautifulSoup(page_words.content, "html.parser")

words_elements = soup2.find_all('strong')

buzz_list = []

for i in words_elements:
    cleaned_words = ''.join(char for char in i.text if char.isalnum() or char.isspace())
    buzz_list.extend(cleaned_words.split())

print(buzz_list)

libray = {'Title': headings_list[2:], 'Post Date': date_list_post, 'End Date': date_list_close}
df = pd.DataFrame(data=libray)

#print(df)