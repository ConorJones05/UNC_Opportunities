import requests
from bs4 import BeautifulSoup
import pandas as pd

links = ['https://catalog.unc.edu/undergraduate/programs-study/biology-major-bs/#requirementstext']

for major in links:
    url = major
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #  finding site
    print(soup.find('table', class_='sc_courselist'))
