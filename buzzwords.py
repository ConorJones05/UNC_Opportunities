import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

try:
    from config import CSV_FILE_PATH
except ImportError:
    CSV_FILE_PATH = None

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

dataframe = {'buzz list': buzz_list}
df=pd.DataFrame(dataframe)

csv_file_path = r'C:\Users\conor\OneDrive\Desktop\UNC_Opportunities\buzzwords.csv'

if CSV_FILE_PATH:
    df.to_csv(CSV_FILE_PATH, index=False)
else:
    print("CSV file path is not set.")