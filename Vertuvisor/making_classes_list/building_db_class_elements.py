import requests
from bs4 import BeautifulSoup
import pandas as pd

block_list = []
df_codes = []
df_names = []
df_credit_hours = []
df_descriptions = []
df_ideas_in_action = []
df_making_connections = []
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
    atozindex = soup.find('div', id='atozindex')
    raw_links = atozindex.find_all('a', href=True)
    for link in raw_links:
        href = link['href']
        full_url = f"https://catalog.unc.edu{href}"
        links.append(full_url)
    print("Finding links task finished")
    return links

def find_course_block(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocks = soup.find_all('div', class_='courseblock')
    for block in blocks:
        block_list.append(block)
    print(f'Found {len(blocks)} blocks from {link}')

def code(block):
    unfiltered = block.find('span', class_="text detail-code margin--tiny text--semibold text--big")
    unfiltered = unfiltered.get_text(strip=True)
    unfiltered = unfiltered.replace(" ", "_")
    filtered = unfiltered.replace(".", "")
    df_codes.append(filtered)

def name(block):
    unfiltered = block.find('span', class_="text detail-title margin--tiny text--semibold text--big")
    unfiltered = unfiltered.get_text(strip=True)
    unfiltered = unfiltered.replace(" ", "_")
    filtered = unfiltered.replace(".", "")
    df_names.append(filtered)

def credit_hours(block):
    unfiltered = block.find('span', class_="text detail-hours margin--tiny text--semibold text--big")
    unfiltered = unfiltered.get_text(strip=True)
    filtered = unfiltered.replace(".", "")
    df_credit_hours.append(filtered)

def desc(block):
    unfiltered = block.find('p', class_="courseblockextra")
    if unfiltered:
        filtered = unfiltered.get_text(strip=True)
        df_descriptions.append(filtered)
    else:
        df_descriptions.append(None)

def ideas_in_action(block):
    unfiltered = block.find('span', class_="text detail-idea_action margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip=True)
        unfiltered = unfiltered.replace('IDEAs in Action Gen Ed:',"")
        unfiltered = unfiltered.replace('.',"")
        if ',' in unfiltered:
            split = unfiltered.split(', ')
            unfiltered = []
            for i in split:
                unfiltered.append(i)
    else:
        unfiltered = None
    df_ideas_in_action.append(unfiltered)

def making_connections(block):
    unfiltered = block.find('span', class_="text detail-making_connections margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip=True)
        unfiltered = unfiltered.replace('Making Connections Gen Ed:',"")
        filtered = unfiltered.replace('.',"")
        if ',' in filtered:
            split = filtered.split(', ')
            filtered = []
            for i in split:
                filtered.append(i)
    else:
        filtered = None
    df_making_connections.append(filtered)

def grading_status(block):
    unfiltered = block.find('span', class_="text detail-grading_status margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip=True)
        unfiltered = unfiltered.replace('Grading Status:',"")
        filtered = unfiltered.replace('.',"")
    else:
        filtered = None
    df_grading_status.append(filtered)

def same_as(block):
    unfiltered = block.find('span', class_="text detail-same_as margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip=True)
        unfiltered = unfiltered.replace('&nbsp;', "")
        filtered = unfiltered.replace('Same as:',"")
        if ',' in filtered:
            split = filtered.split(', ')
            filtered = []
            for i in split:
                filtered.append(i)
    else:
        filtered = None
    df_same_as.append(filtered)

def requisites(block):
    unfiltered = block.find('span', class_="text detail-requisites margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip=True)
    df_requisites.append(unfiltered if unfiltered is not None else None)

def global_language(block):
    unfiltered = block.find('span', class_="text detail-global_language margin--default")
    if unfiltered is not None:
        unfiltered = unfiltered.get_text(strip=True)
        unfiltered = unfiltered.replace('Global Language:',"")
        unfiltered = unfiltered.replace('.',"")
    df_global_language.append(unfiltered if unfiltered is not None else None)

# Get all course links


find_course_block('https://catalog.unc.edu/courses/wolo/')

# Process each block to collect course information
for block in block_list:
    code(block)
    name(block)
    credit_hours(block)
    desc(block)
    ideas_in_action(block)
    making_connections(block)
    grading_status(block)
    same_as(block)
    requisites(block)
    global_language(block)

# Create the DataFrame
dict = {"Code": df_codes, "Names": df_names, "Credit Hours": df_credit_hours, "Description": df_descriptions,
        "Ideas": df_ideas_in_action, "Connections": df_making_connections, 
        "Grading Status": df_grading_status, "Same As": df_same_as, 
        "Requisites": df_requisites, "Global Language": df_global_language}


# Display the DataFrame
dataframe = pd.DataFrame(dict)

print(dataframe.head)