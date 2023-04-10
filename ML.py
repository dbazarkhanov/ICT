from sklearn import linear_model
import numpy as np

array = np.array(['1', '5', '9', '11', '45', '78'])
array2 = np.array(['2', '6', '10', '12', '46', '79'])
# print(array.reshape(3, 2))
print(np.dstack([array, array2]))
print(np.vstack([array, array2]))
print(np.hstack([array, array2]))