from bs4 import BeautifulSoup 
from selenium import webdriver

email_list = []
driver = webdriver.Firefox()

driver.get("https://dir.unc.edu/detail/b85e4823caed11ff504380ac675c0a7ecc466e90d73ec40a609ff6e73a380c6fa823d321d2f39cdd641df0c521a191f5")
print(driver.current_url)
html_content = driver.page_source
driver.quit()


soup = BeautifulSoup(html_content, "html.parser")
a_elements = soup.find_all('a', href=True)  # Limit to anchor tags with href attribute
for a in a_elements:
    if 'mailto:' in a['href']:  # Check if the anchor tag contains an email address
        email_list.append(a.text.strip())  # Extract email address text
print(email_list)