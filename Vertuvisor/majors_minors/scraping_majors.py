import requests
from bs4 import BeautifulSoup

def findURLS_majors():
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
    majors_bycat = {'Arts': Arts, 'Science': Science}
    minors = []

    for major in list_of_major_and_minors:
        if 'Major' in major:
            if 'B.A.' in major:
                curent_class = major.replace(",", ":")
                curent_class = major.replace("-", "- ")
                Arts.append(curent_class)
            elif 'B.S.' in major:
                curent_class = major.replace(",", ":")
                curent_class = major.replace("-", "- ")
                Science.append(curent_class)
            else:
                assert "No BA or BS"
        elif 'Minor' in major:
            curent_class = major.replace(",", ":")
            curent_class = major.replace("-", "- ")
            minors.append(curent_class)

    lowercase_majors_and_minors = [x.lower() for x in list_of_major_and_minors]
    

    return majors_bycat, minors

print(findURLS_majors())
