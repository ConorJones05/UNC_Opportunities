from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
import time


driver = webdriver.Firefox()

a_lis = ['Anika Ahmed','Laine Albright', 'Alina Atzor', 'Anne Barnes', 'Charlotte Brown',
'Emma Brown',
'Mary-Katherine Bryant',
'Taylor Campbell',
'Isabella Carvajal-Guillem',
'Florence Castle',
'Davis Cooke',
'Caitlin Davis',
'Jada Day',
'Madilyn Deifell',
'Firona Dong',
'Rebekah Elam',
'Bilal Eltohami',
'Kinleigh Erwin',
'Sarah Fenwick',
'Martha Fisher',
'Elena Ginter',
'Jamie Grant',
'Madeleine Hadrys',
'Brandon Henderson',
'Maelynn Higgins',
'Clairmel Hjardemaal',
'Jacob Hoffman',
'Jeremy Hu',
'Meghan Hughes',
'Kellyn Jiles',
'Bailey Joiner',
'Conor Jones',
'Harrison Jordan',
'John Kenkel',
'Ian Langston',
'Ashley Lazaro',
'Destiny Lindsey',
'Kameron Mallory',
'Andreea Mccoy',
'Micah Miller',
'Lindsey Muratore',
'Stephanie Murcia-Castro',
'Ruby Narte',
'Seton Pajibo',
'Nidh Patel',
'Hailey Paul',
'Carson Perkins',
'Andrew Plaisted',
'Nathaniel Pope',
'Lance Rainer',
'Leon Rodriguez-Jarquin',
'Amaya Sales',
'Lilly Shapiro',
'Noni Shemenski',
'Yosabet Sima',
'Ella Simmons',
'Ryann Tighe',
'Abigail Tirone',
'Christian Tyler',
'Dana Vernon',
'Gerardo Villacis',
'Isaac Weiss',
'Jackson Wetherbee']
email_list = []

for e in a_lis:
     driver.get("https://dir.unc.edu/")
     inputElement = driver.find_element(By.ID, "input-15")
     inputElement.send_keys(e)
     inputElement.send_keys(Keys.ENTER)
     time.sleep(1)
     html_content = driver.page_source


     soup = BeautifulSoup(html_content, "html.parser")
     a_elements = soup.find_all('a', href=True)  # Limit to anchor tags with href attribute
     for a in a_elements:
        if 'mailto:' in a['href']:  # Check if the anchor tag contains an email address
            email_list.append(a.text.strip())
print(email_list)