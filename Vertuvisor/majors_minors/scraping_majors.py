import requests
from bs4 import BeautifulSoup
import pandas as pd

def majors_and_names() -> list[str]:
    URL = "https://catalog.unc.edu/undergraduate/programs-study/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #  Pulling of HTML 
    list_of_major_and_minors = []
    sections = soup.find_all('h2', class_='letternav-head')
    for section in sections:
        ul = section.find_next('ul')
        items = ul.find_all('li')
        for item in items:
            list_of_major_and_minors.append(item.text.strip())
    #  Makes an unfiltered list of all majors and minors from the website
    return list_of_major_and_minors


def cleaning_majors_minors(names):
    arts = []
    science = []
    minors = []
    for major in names:
        if 'Major' in major:
            if 'B.A.' in major:
                arts.append(major)
            elif 'B.S.' in major:
                science.append(major)
        elif 'Minor' in major:
            minors.append(major)
    #  Spilting the diffrent majors/minors into diffrent lists

    return arts, science, minors




def make_URL():    
    links = []
    for section in sections:
        ul = section.find_next('ul')
        items = ul.find_all('li')
        for item in items:
            links.append(item.text.strip())

    return links

print(cleaning_majors_minors(majors_and_names()))