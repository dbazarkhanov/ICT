import numpy as np
import sklearn.linear_model as skmodel
import sklearn.preprocessing as skpepro
import sklearn.model_selection as skselection
import matplotlib.pyplot as plt

data_x = np.random.normal(9, 4, 100).reshape(-1,1)
data_y = np.random.randint(20,180, size = (len(data_x)))/100*(data_x*data_x*8 + 2*data_x + 5).reshape(-1,1)

data_x_train = data_x[:80]
data_x_test = data_x[80:]
data_y_train = data_y[:80]
data_y_test = data_y[80:]

data_x_train, data_x_test, data_y_train, data_y_test = skselection.train_test_split(
    data_x, data_y, train_size=0.75, shuffle=True)

# plt.scatter(data_x_train, data_y_train)
# plt.scatter(data_x_test, data_y_test)
# plt.show()

data_x_train = skpepro.PolynomialFeatures(degree=2, include_bias=False).fit_transform(data_x)
model = skmodel.LinearRegression().fit(data_x_train, data_y_train)

plt.scatter(data_x_train, data_y_train)
plt.scatter(data_x_test, data_y_test)
plt.show()