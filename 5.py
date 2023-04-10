import matplotlib.pyplot as plt
import seaborn
import pandas as pd

df_origin = pd.read_parquet('df_final_US_EUR.parquet')

df = df_origin[df_origin['Name'] == 'GOOGL']
df.reset_index(drop=True, inplace=True)

#df.plot(y = 'Open')

#you can also use another column as x axis
#df.plot(x = 'Date', y = 'Close')

#You can select a smaller amount of data
#import datetime
#df_small = df[df['Date'] > datetime.datetime(2022,8,1)]

#use the bar kind
#use the kind attribute
#df_small.plot(kind = 'bar', x = 'Date', y = 'Volume')

#use the horizontal bar kind
#df_small.plot(kind = 'barh', x = 'Date', y = 'Volume')

# use the histogram
#df_small.plot(kind = 'hist', y = ['Open', 'Close'])

# use the boxplot (kind  = 'box')
#df_small.plot(kind = 'box', y = ['Open', 'Close'])


# use the area
#df_small.plot(kind = 'area', y = ['Open', 'Close'])



#the scatter version
#df_small.plot(kind = 'scatter', x = 'Close', y = 'Open')



#YOUR TURN (15 minutes)(with my parquet file install pyarrow and fastparquet package first)
#) or any csv data (price))
#%matplotlib inline
#Draw the evolution of the volume with the date in line
#Draw the scatter plot of the volume in function of the Open price
#import matplotlib.pyplot as plt
#plt.show()

df_origin = pd.read_csv('airbus_price.csv')

df_origin.plot(x = 'Volume', y = 'Date')
plt.show()
df_origin.plot(kind = 'scatter', x = 'Volume', y = 'Open')

col = ['Open', 'High', 'Low', 'Close', 'Volume']
perc = []
for index, line in df.iterrows():
    if index == 0:
        perc.append(0)
    else:
        perc.append((line['Volume'] - df.loc[index-1, 'Volueme'])/line['Volume'] *100)
        
df['perc_Volume'] = perc
print(df)