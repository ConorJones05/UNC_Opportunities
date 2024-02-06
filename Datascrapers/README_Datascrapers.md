# Data Scraper for UNC Opportunities Board

## Overview
This Python script scrapes information from the [UNC Opportunities Board](https://our.unc.edu/find/opportunities/) and analyzes the content for relevance to data science terms. Additionally, it fetches key terms from a [blog post](https://www.blog.dailydoseofds.com/p/75-key-terms-that-all-data-scientists) to evaluate the fit of the scraped opportunities with data science terminology.

## Prerequisites
- Python 3.x
- Install required libraries using:
  ```bash
  pip install requests
  pip install beautifulsoup4
  pip install pandas
  ```

## Usage
1. Run the script by executing the following command:
   ```bash
   python data_scraper.py
   ```
2. The script will print a DataFrame containing the scraped data, including the title of opportunities, post date, end date, and a fit score based on data science terminology.

## Code Explanation
- The script utilizes the `requests`, `BeautifulSoup`, `re`, and `pandas` libraries.
- It fetches information from the UNC Opportunities Board page and extracts titles, post dates, and end dates.
- Key terms for data science are fetched from a blog post and filtered to create a relevant keyword list.
- The script then calculates the fit score for each opportunity based on the presence of data science terms.
- The final results are presented in a DataFrame for easy analysis.
