'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import pandas as pd
import csv
import datetime
import numpy as np

missing_values = ['_', 'error']
df = pd.read_csv('attendance_to_clean.csv', na_values=missing_values)

for i, lines in df.iterrows():
    try:
        int(lines['NAME_STUDENT'])
        df.loc[i, 'NAME_STUDENT'] = np.nan
    except:
        pass

for i, lines in df.iterrows():
    try:
        datetime.datetime.strptime(lines['DATE'], '%Y-%m-%d')
    except: 
        df.loc[i, 'DATE'] = np.nan

for i, lines in df.iterrows():
    try:
        int(lines['COUNT'])
        pass
    except:
        df.loc[i, 'COUNT'] = np.nan

for i, lines in df.iterrows():
    try:
        if df.loc[i, 'BEGIN_HOUR'] > 17:
            df.loc[i, 'BEGIN_HOUR'] = np.nan
        if df.loc[i, 'COUNT'] > 2 or df.loc[i, 'COUNT'] < 1:
            df.loc[i, 'COUNT'] = np.nan
    except:
        pass

for i, lines in df.iterrows():
    try:
        if df.loc[i, 'WEEK'] > float(8):
            df.loc[i, 'WEEK'] = np.nan
    except:
        pass
# print(df.sort_values(by=['BEGIN_HOUR']))

df.loc[1007, 'DATE'] = np.nan
df.loc[3369, 'DATE'] = np.nan
df.loc[1162, 'DATE'] = np.nan

# print(df.isnull().sum().sum())

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.sort_values(by=['NAME_STUDENT', 'DATE', 'BEGIN_HOUR', 'WEEK'], inplace=True)
df.reset_index(drop=True, inplace=True)

# print(df.sort_values(by=['DATE']))
print(df)