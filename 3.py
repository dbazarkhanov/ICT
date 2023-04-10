import pandas as pd
import numpy as np
import datetime

missing_values = ['na', '--', 'ERROR', '']
df = pd.read_csv('Apple_price_to_clean.csv', na_values=missing_values)

for index, lines in df.iterrows():
    try:
        a = int(lines['Date'])
        #print(a)
        df.loc[index, 'Date'] = np.nan
    except:
        pass

#print(df)

# print(df.isnull().sum())

missing_values = ['--', 'na']
df = pd.read_csv('csv_to_clean.csv', na_values=missing_values)

df.fillna(method='ffill')
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)