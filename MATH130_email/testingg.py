from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
import time


driver = webdriver.Firefox()

a_lis = ['Jackson Wetherbee']
email_list = []

for e in a_lis:
     driver.get("https://dir.unc.edu/")
     inputElement = driver.find_element(By.ID, "input-15")
     inputElement.send_keys(e)
     inputElement.send_keys(Keys.ENTER)
     time.sleep(1)
     html_content = driver.page_source
     print(html_content)


     soup = BeautifulSoup(html_content, "html.parser")
     a_elements = soup.find_all('a', href=True)  # Limit to anchor tags with href attribute
     for a in a_elements:
        if 'mailto:' in a['href']:  # Check if the anchor tag contains an email address
            email_list.append(a.text.strip())
print(email_list)