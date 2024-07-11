import smtplib, ssl
from config import SENDER_EMAIL, RECEIVER_EMAIL, APP_PASSWORD
import datetime
import pandas as pd
from uncdatabase import df

try:
    old_file = pd.read_csv('opportunities.csv')
except FileNotFoundError:
    old_file = pd.DataFrame()  # Create an empty DataFrame if file not found

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = SENDER_EMAIL  # Enter your address
receiver_email = RECEIVER_EMAIL  # Enter receiver address
password = APP_PASSWORD #  Enter app password

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
    except Exception as e:
        print(f"An error occurred: {e}")
    df.to_csv('opportunities.csv', index=False)
else:
    print("No new opportunities.")
