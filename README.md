Certainly! Here is the cleaned-up README without the actual script code:

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

## Setting Up a Cron Job (Linux/macOS)

To automate the execution of your scripts, you can set up a cron job.

### Step-by-Step Guide

1. **Open the Crontab Editor:**
   ```bash
   crontab -e
   ```

2. **Add a New Cron Job:**
   Add the following lines to schedule your scripts. This example runs the main scraper script every day at 8 AM and the buzzwords updater every Sunday at 9 AM.

   ```bash
   # Run main scraper script daily at 8 AM
   0 8 * * * /usr/bin/python3 /path/to/your/main_script.py

   # Run buzzwords updater script every Sunday at 9 AM
   0 9 * * 0 /usr/bin/python3 /path/to/your/buzzwords_updater.py
   ```

   Make sure to replace `/usr/bin/python3` with the path to your Python interpreter and `/path/to/your/` with the path to your script files.

3. **Save and Exit:**
   Save the changes and exit the editor (usually by pressing `CTRL+O` to save and `CTRL+X` to exit in nano).

### Checking the Cron Job (macOS)

On macOS, you can also use the `launchd` system to schedule tasks. However, using cron is simpler for most basic tasks. Here’s how you can check your cron jobs:

```bash
crontab -l
```

This command lists all the cron jobs for the current user.

## Summary
This project automates the process of scraping opportunities from the UNC Opportunities Board and notifies users via email if new opportunities are found. It also keeps a list of buzzwords up to date for filtering opportunities. Ensure you configure the `config.py` file and have the necessary libraries installed before running the scripts.

Additionally, setting up a cron job allows for the automation of running these scripts at specified intervals, ensuring the data and notifications are always up to date.
