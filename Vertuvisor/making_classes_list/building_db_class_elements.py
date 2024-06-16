import requests
from bs4 import BeautifulSoup
import pandas as pd

block_list = []
df_codes = []
df_names = []
df_credit_hours = []
df_ideas_in_action = []
df_ideas_in_action_amount = []
df_making_connections = []
df_making_connections_amount = []
df_grading_status = []
df_same_as =[]
df_requisites = []
df_global_language = []

def links():
    URL = "https://catalog.unc.edu/courses/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # Pulling of HTML 
    links = []
    atozindex = soup.find('div', id = 'atozindex')
    raw_links = atozindex.find_all('a', href = True)
    for link in raw_links:
        href = link['href']
        full_url = f"https://catalog.unc.edu{href}"
        links.append(full_url)
    print("Finding links task finsihed")
    return links

def find_course_block(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocks = soup.find_all('div', class_ = 'courseblock')
    for block in blocks:
        block_list.append(block)

def code(block):
    unfiltered = block.find('span', class_ = "text detail-code margin--tiny text--semibold text--big")
    unfiltered = unfiltered.get_text(strip=True)
    unfiltered = unfiltered.replace(" ", "_")
    filtered = unfiltered.replace(".", "")
    df_codes.append(filtered)


def name(block):
    unfiltered = block.find('span', class_ = "text detail-title margin--tiny text--semibold text--big")
    unfiltered = unfiltered.get_text(strip=True)
    unfiltered = unfiltered.replace(" ", "_")
    filtered = unfiltered.replace(".", "")
    df_names.append(filtered)


def credit_hours(block):
    unfiltered = block.find('span', class_ = "text detail-hours margin--tiny text--semibold text--big")
    unfiltered = unfiltered.get_text(strip=True)
    filtered = unfiltered.replace(".", "")
    df_credit_hours.append(filtered)


def desc(block):
    unfiltered = block.find('p', class_ = "courseblockextra")
    filtered = unfiltered.get_text(strip=True)
    df_credit_hours.append(filtered)


def ideas_in_action(block):
    unfiltered = block.find('span', class_="text detail-idea_action margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip = True)
        unfiltered = unfiltered.replace('IDEAs in Action Gen Ed:',"")
        filtered = unfiltered.replace('.',"")
    if ',' in filtered:
        split = filtered.split(', ')
        filtered = []
        for i in split:
            filtered.append(i)
    df_ideas_in_action_amount.append(len(filtered))
    df_ideas_in_action.append(filtered)
    

def making_connections(block):
    unfiltered = block.find('span', class_="text detail-making_connections margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip = True)
        unfiltered = unfiltered.replace('Making Connections Gen Ed:',"")
        filtered = unfiltered.replace('.',"")
    if ',' in filtered:
        split = filtered.split(', ')
        filtered = []
        for i in split:
            filtered.append(i)
    df_making_connections_amount.append(len(filtered))
    df_making_connections.append(filtered)

def grading_status(block):
    unfiltered = block.find('span', class_="text detail-grading_status margin--default")
    unfiltered = unfiltered.get_text(strip = True)
    unfiltered = unfiltered.replace('Grading Status:',"")
    filtered = unfiltered.replace('.',"")
    df_grading_status.append(filtered)


def same_as(block):
    unfiltered = block.find('span', class_="text detail-same_as margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip = True)
        unfiltered = unfiltered.replace('&nbsp;', "")
        filtered = unfiltered.replace('Same as:',"")
    if ',' in filtered:
        split = filtered.split(', ')
        filtered = []
        for i in split:
            filtered.append(i)
    df_same_as.append(filtered)


def requisites(block):
    unfiltered = block.find('span', class_="text detail-requisites margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip = True)
    df_requisites.append(unfiltered)


def global_language(block):
    unfiltered = block.find('span', class_="text detail-global_language margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip = True)
        unfiltered = unfiltered.replace('Global Language:',"")
        unfiltered = unfiltered.replace('.',"")
    df_global_language.append(unfiltered)


all_blocks = find_course_block('https://catalog.unc.edu/courses/wolo/')

for block in block_list:
    code(block)
    name(block)
    


pd.DataFrame()

