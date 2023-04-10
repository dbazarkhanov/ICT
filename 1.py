import requests 
import io 
import pandas as pd
import datetime

origin = datetime.datetime(2021,1,1)
begin = datetime.datetime(2021,1,5)
delta = begin -origin
delta = delta.total_seconds()

print(delta)

params = {'period1': str(int(delta)),'period2': '1664912171','interval':'1d','events':'history','includeAdjustedClose':'true'}

url = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
resp = requests.get(url, headers=headers, params=params)
df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
#print(df)
print(resp.content)