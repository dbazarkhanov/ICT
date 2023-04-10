from bs4 import BeautifulSoup
import requests

url = 'https://news.google.com/search?for=microsoft&hl=en-US&gl=US&ceid=US:en'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.content, features='html.parser')
attrs = {'class':'gb_Cc'}

# print(soup.find_all('h3')[0].find_all('a')[0].contents)
# print(soup.find_all('h3')[0].find_all('a')[0].find_all('href='))
print(soup.find_all('div', attrs))