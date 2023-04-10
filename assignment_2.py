
'''
The objective of this assignment is to print the dataframe showed in the instruction.
Only one test will be done.
You can write you code after this comment :
'''
#Your code here:

import pandas as pd

df = pd.DataFrame({'Name':pd.Series(['Brad', 'Angelina', 'Tom'], [0, 1, 2]),
    'Surname':pd.Series(['Pitt', 'Jolie', 'Cruise'], [0, 1, 2]),
    'Age':pd.Series([58, 47, 60], [0, 1, 2])
    })

print(df)