import pandas as pd
import numpy as np

df_all = pd.read_parquet('df_final_US_EUR.parquet')

df = df_all[df_all['Name'] == 'AAPL']
# df.reset_index(drop=True, inplace=True)

# columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# for p in columns:
#     perc = []
#     for i, l in df.iterrows():
#         if i == 0: perc.append(0)
#         else: perc.append((l[p]-df.loc[i-1, p])/l[p]*100)
#     df['perc'+p] = perc
    # df.loc[0, 'perc'+p] = np.nan

# for i, l in df.():
#     if df.loc[i, 'percVolume'] <= float(0):
#         df.loc[i, 'percVolume'] = np.nan
#     if df.loc[i, 'percClose'] <= float(0):
#         df.loc[i, 'percClose'] = np.nan

print(df_all[df_all['Volume'] > 0])
print(df_all[df_all['Volume'] <= 0].count())

#print(df)
# print(df.isnull().sum())

df.dropna(inplace=True)
#print(df)