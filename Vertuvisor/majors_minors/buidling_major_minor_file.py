import requests
from bs4 import BeautifulSoup
import pandas as pd

def majors_and_names() -> list[str]:
    URL = "https://catalog.unc.edu/undergraduate/programs-study/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # Pulling of HTML 
    list_of_major_and_minors = []
    sections = soup.find_all('h2', class_='letternav-head')
    for section in sections:
        ul = section.find_next('ul')
        items = ul.find_all('li')
        for item in items:
            list_of_major_and_minors.append(item.text.strip())
    print(f"Section 1/3 is {int((len(list_of_major_and_minors) / 185) * 100)}% complete")
    # Makes an unfiltered list of all majors and minors from the website
    return list_of_major_and_minors


def major_minor_links():
    URL = "https://catalog.unc.edu/undergraduate/programs-study/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # Pulling of HTML 
    links = []
    all_links = soup.find_all('a', href = True)
    for link in all_links:
        href = link['href']
        if href.startswith('/undergraduate/programs-study/') and not href.startswith('#'):
            full_url = f"https://catalog.unc.edu{href}#requirementstext"
            links.append(full_url)
        print(f"Section 2/3 is {int((len(links) / 188) * 100)}% complete")

    return links[1:186]


def total_hours(links):
    total_hours_list = []
    for url in links:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        hours_elements = soup.find_all('td', class_='hourscol')
        if len(hours_elements) > 0:
            hours_elements = hours_elements[-1]
        else:
            hours_elements = "Error"
        if hours_elements == "Error":
            hours = hours_elements
        else:
            hours = hours_elements.text.strip()
        total_hours_list.append(hours)
        print(f"Section 3/3 is {int((len(total_hours_list) / 185) * 100)}% complete")
    return total_hours_list





pandas_df = {'Name': majors_and_names(), 'Total_Hours': total_hours(major_minor_links()), 'Link': major_minor_links()}
Dataframe = pd.DataFrame(pandas_df)

Dataframe.head