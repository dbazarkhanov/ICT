import requests
from bs4 import BeautifulSoup

url = 'https://api.thecatapi.com/v1/images/search'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

resp = requests.get(url, headers=headers)

# print(resp.content)

