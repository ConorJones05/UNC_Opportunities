# README for UNC Opportunities Board Email Sender

## Overview
This project automates the process of sending email notifications for new opportunities scraped from the UNC Opportunities Board. It filters opportunities based on predefined buzzwords and sends email notifications using Python scripts.

## Requirements
- Python 3.6+
- Required libraries: `smtplib`, `ssl`, `pandas`
- An app password for your email account (if using Gmail, this is necessary for SMTP authentication)

## Setup

1. **Install Required Libraries:**
   ```bash
   pip install pandas requests BeautifulSoup
   ```
   
2. **Create a Gmail Account and App Password**
   - To automate email, you must create a Gmail account to send the email from. Follow the instructions [here](https://support.google.com/mail/answer/56256?hl=en) to create an account.
   - You must also create an app password to allow the script to access the account. Follow the instructions [here](https://support.google.com/mail/answer/185833?hl=en) to create an app password.

4. **Configuration:**
   Create a `config.py` file with the following content:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   RECEIVER_EMAIL = "receiver_email@gmail.com"
   APP_PASSWORD = "your_app_password"
   ```

5. **Running the Email Sender Script:**

### Main Script (Email Sender)
The email sender script performs the following tasks:
- Reads the list of opportunities from `opportunities.csv`.
- Sends an email notification for each new opportunity found since the last run.

## Setting Up Automation

### Task Scheduler (Windows)

To automate the execution of the email sender script on Windows, you can use Task Scheduler.

#### Step-by-Step Guide

1. **Open Task Scheduler:**
   - Press `Win + R`, type `taskschd.msc`, and press Enter to open the Task Scheduler.

2. **Create a Basic Task:**
   - In the Task Scheduler window, click on "Create Basic Task" in the Actions panel.
   - Give your task a name and description, then click "Next".

3. **Set the Trigger:**
   - Choose how often you want the task to run (daily, weekly, etc.), then click "Next".
   - Set the start date and time for when you want the task to begin, then click "Next".

4. **Start a Program:**
   - Select "Start a Program" and click "Next".

5. **Program/Script:**
   - Browse to your Python executable (e.g., `C:\Python39\python.exe`).
   - In the "Add arguments" field, type the path to your email sender script (e.g., `C:\path\to\your\email_sender.py`).
   - In the "Start in" field, type the directory where your email sender script is located (e.g., `C:\path\to\your`).

6. **Finish:**
   - Review your settings and click "Finish" to create the task.

#### Example: Setting Up Task Scheduler for Daily Script Execution

1. **Create Basic Task:**
   - Name: `UNC Opportunities Email Sender`
   - Description: `Sends email notifications for new opportunities daily`

2. **Set Trigger:**
   - Daily
   - Start date: `07/11/2024`
   - Start time: `08:00 AM`

3. **Action: Start a Program**
   - Program/Script: `C:\Python39\python.exe`
   - Add arguments: `C:\path\to\your\email_sender.py`
   - Start in: `C:\path\to\your`

4. **Finish:**
   - Review the task summary and click "Finish".

### cron (Unix-based Systems)

To automate the execution of the email sender script on Unix-based systems like Linux or macOS, you can use cron.

#### Step-by-Step Guide

1. **Open Crontab Editor:**
   - Open a terminal window.

2. **Edit Crontab:**
   - Type `crontab -e` and press Enter.

3. **Add a New Cron Job:**
   - Add the following line to schedule your email sender script. This example runs the script daily at 8 AM.

     ```bash
     # Run email sender script daily at 8 AM
     0 8 * * * /usr/bin/python3 /path/to/your/email_sender.py
     ```

   - Make sure to replace `/usr/bin/python3` with the path to your Python interpreter and `/path/to/your/` with the path to your script file.

4. **Save and Exit:**
   - Save the changes and exit the editor (usually by pressing `CTRL+O` to save and `CTRL+X` to exit in nano).

## Summary
This project automates the process of sending email notifications for new opportunities scraped from the UNC Opportunities Board. Ensure you configure the `config.py` file and have the necessary libraries installed before running the email sender script.
