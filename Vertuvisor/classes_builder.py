import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://catalog.unc.edu/courses/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all("a", href=True)

subpage_urls = []
for link in links:
    href = link['href']
    if not href.startswith('http'):
        absolute_url = urljoin(URL, href)
        subpage_urls.append(absolute_url)

for subpage_url in subpage_urls:
    subpage_response = requests.get(subpage_url)
    subpage_html_content = subpage_response.content
    subpage_soup = BeautifulSoup(subpage_html_content, 'html.parser')
