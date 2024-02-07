"""UCS Tution Cost Datascraper"""
import pandas as pd
from bs4 import BeautifulSoup  
url = 'UCS_2024_Spring/COLLEGE MATRICULATION 2018–2023_ Durham Academy  - Sheet1.csv'
df = pd.read_csv(url,index_col=0)
df['Amout of Students'].fillna(1, inplace=True)
df['Amout of Students'] = df['Amout of Students'].astype(int)
print(df)



















