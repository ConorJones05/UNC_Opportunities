# README for UNC Opportunities Board Data Scraper

## Overview
This project is a data scraper for the UNC Opportunities Board, which collects opportunities listed on the board and sends an email notification if new opportunities are found. The scraper also includes functionality to update a list of buzzwords used for filtering and evaluating the opportunities.

## Requirements
- Python 3.6+
- Required libraries: `requests`, `beautifulsoup4`, `pandas`, `smtplib`, `ssl`
- An app password for your email account (if using Gmail, this is necessary for SMTP authentication)

## Setup

1. **Install Required Libraries:**
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

2. **Configuration:**
   Create a `config.py` file with the following content:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   RECEIVER_EMAIL = "receiver_email@gmail.com"
   APP_PASSWORD = "your_app_password"
   ```

3. **Buzzwords File:**
   Create a CSV file named `buzzwords.csv` with a column `buzz_list` that contains buzzwords for filtering opportunities.

## Running the Scraper

### Main Script
The main script performs the following tasks:

1. **Scrape the UNC Opportunities Board:**
   - Collects the titles and dates of the opportunities.
   - Filters and counts relevant buzzwords in the descriptions.

2. **Compare with Previous Data:**
   - Checks if there are new opportunities compared to the last run.
   - If new opportunities are found, sends an email notification.

3. **Email Notification:**
   - Sends an email with the details of the new opportunity.

4. **Update CSV File:**
   - Saves the current list of opportunities to `opportunities.csv`.

### Code
```python
import smtplib, ssl
from config import SENDER_EMAIL, RECEIVER_EMAIL, APP_PASSWORD
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from uncdatabase import df  # Assuming this is a module you have for handling data

# Scrape opportunities
buzz_list = pd.read_csv("buzzwords.csv")['buzz_list'].tolist()
URL = "https://our.unc.edu/find/opportunities/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Extract titles and dates
h1_elements = soup.find_all("h1")
date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
date_elements = soup.find_all("div", class_="col-md-10")

headings_list = [h1.text.strip() for h1 in h1_elements]
date_list = [date.text.strip() for date in date_elements if date_pattern.match(date.text.strip())]

date_list_post = [date_list[i] for i in range(len(date_list)) if i % 2 == 0]
date_list_close = [date_list[i] for i in range(len(date_list)) if i % 2 == 1]

# Extract and filter descriptions
result_list = []
for i in range(len(date_elements)):
    paragraphs = date_elements[i].find_all('p')
    div_row_result = [p.text.strip() for p in paragraphs]
    result_list.append(div_row_result)

comp_list = [result for result in result_list if len(result) > 0]

# Calculate fit score based on buzzwords
fit_array = []
for comp in comp_list:
    fit_number = 0
    split_list = str(comp).lower().split()
    for word in split_list:
        if word in buzz_list:
            fit_number += 1
    fit_array.append(fit_number)

# Create DataFrame and compare with old data
dataframe = {'Title': headings_list[2:], 'Post_Date': date_list_post, 'End_Date': date_list_close, 'Fit': fit_array}
df = pd.DataFrame(dataframe)

try:
    old_file = pd.read_csv('opportunities.csv')
except FileNotFoundError:
    old_file = pd.DataFrame()  # Create an empty DataFrame if file not found

if not df.equals(old_file):
    opportunity = df.iloc[0]
    title = opportunity['Title']
    post_date = opportunity['Post_Date']
    end_date = opportunity['End_Date']
    fit = opportunity['Fit']
    
    message = f"""\
Subject: New Opportunities: {datetime.date.today()}

There has been a new opportunity posted:

Title: {title}
Post Date: {post_date}
End Date: {end_date}
Fit: {fit}
https://our.unc.edu/find/opportunities/
"""
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
        df.to_csv('opportunities.csv', index=False)
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No new opportunities.")
```

### Buzzwords Updater
This script updates the list of buzzwords by scraping a blog post.

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    from config import CSV_FILE_PATH
except ImportError:
    CSV_FILE_PATH = None

URL2 = "https://www.blog.dailydoseofds.com/p/75-key-terms-that-all-data-scientists"
page_words = requests.get(URL2)
soup2 = BeautifulSoup(page_words.content, "html.parser")

words_elements = soup2.find_all('strong')

buzz_unfiltered = [''.join(char for char in i.text if char.isalnum() or char.isspace()) for i in words_elements]
buzz_list = [word.lower() for word in buzz_unfiltered if word.lower() not in ["the", "is", "of", "and", "a", "in", "that", "it", 'this', 'what']]

df = pd.DataFrame({'buzz_list': buzz_list})

csv_file_path = r'C:\Users\conor\OneDrive\Desktop\UNC_Opportunities\buzzwords.csv'
if CSV_FILE_PATH:
    df.to_csv(CSV_FILE_PATH, index=False)
else:
    print("CSV file path is not set.")
```

### Running the Buzzwords Updater
To run the buzzwords updater script:
```bash
python buzzwords_updater.py
```

## Summary
This project automates the process of scraping opportunities from the UNC Opportunities Board and notifies users via email if new opportunities are found. It also keeps a list of buzzwords up to date for filtering opportunities. Ensure you configure the `config.py` file and have the necessary libraries installed before running the scripts.
