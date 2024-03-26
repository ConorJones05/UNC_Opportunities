import requests
from bs4 import BeautifulSoup

def findURLS():
    URL = "https://catalog.unc.edu/undergraduate/programs-study/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    list_of_major_and_minors = []
    sections = soup.find_all('h2', class_='letternav-head')
    for section in sections:
        ul = section.find_next('ul')
        items = ul.find_all('li')
        for item in items:
            list_of_major_and_minors.append(item.text.strip())

    Arts = []
    Science = []
    majors_bycat = [Arts, Science]
    minors = []

    for major in list_of_major_and_minors:
        if 'Major' in major:
            if 'B.A.' in major:
                Arts.append(major)
            elif 'B.S.' in major:
                Science.append(major)
            else:
                assert "No BA or BS"
        elif 'Minor' in major:
            minors.append(major)

    lowercase_majors_and_minors = [x.lower() for x in list_of_major_and_minors]
    

    return majors_bycat, minors

print(findURLS())
