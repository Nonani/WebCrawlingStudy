import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.naver.com/')
# print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find('title')
print(title.get_text())
