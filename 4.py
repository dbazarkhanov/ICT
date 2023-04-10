import pandas as pd
import csv

all_data = []  
with open('list_symbols_US.csv', 'r') as US, open('list_symbols_euronext.csv', 'r') as EU:
    for i in csv.reader(US, delimiter=','):
        for j in i:
            all_data.append(j)
    for i in csv.reader(EU, delimiter=','):
        for j in i:
            all_data.append(j)

for i in range(10):
    url = 'https://query1.finance.yahoo.com/v7/finance/download/SYM?period1=0&period2=1661904000&interval=1d&events=history&includeAdjustedClose=true'
    url.replace('SYM', all_data[i])
    df = pd.read_csv(url)

print(df)
# df['NUM_BEDROOMS'].fillna(method = 'bfill', inplace = True)