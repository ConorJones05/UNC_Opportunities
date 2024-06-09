import requests
from bs4 import BeautifulSoup

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
    # Makes an unfiltered list of all majors and minors from the website
    return list_of_major_and_minors

def make_URL(names):
    links = []
    for name in names:
        formatted_name = name.lower()
        formatted_name = formatted_name.replace('and', '')
        formatted_name = formatted_name.replace('for', '')
        formatted_name = formatted_name.replace(' ', '-')
        formatted_name = formatted_name.replace(',', '')
        formatted_name = formatted_name.replace('.', '')
        formatted_name = formatted_name.replace('--', '-')
        formatted_name = formatted_name.replace("'", '')
        links.append(f"https://catalog.unc.edu/undergraduate/programs-study/{formatted_name}/")
    return links

def test_urls(links):
    broken = []
    for url in links:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"URL works: {url}")
        else:
            print(f"Page not found for URL: {url}, Status Code: {response.status_code}")
            striped_url = url.replace("https://catalog.unc.edu/undergraduate/programs-study/", '')
            striped_url = striped_url.replace('/', '')
            broken.append(striped_url)
    print('')
    print('')
    print('')
    print('******************************************************')
    print(f"{len(broken)} links are broken")
    print(f"{(len(links) - len(broken)) / len(links) * 100:.2f}% correct")
    print(broken)

names = majors_and_names()
urls = make_URL(names)
test_urls(urls)
