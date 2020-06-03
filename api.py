import requests
from bs4 import BeautifulSoup

s = requests.Session()

url = 'https://sell.smartstore.naver.com/#/sellers/store/detail/api'
r = requests.get(url, allow_redirects=True)
api_id - 'QXac6u4r'
soup = BeautifulSoup(r.text)

s = soup.find_all('wb')
print(s)
