import numpy as np
import sklearn.linear_model as skmodel
import sklearn.preprocessing as skpepro
import matplotlib.pyplot as plt

x = np.array([6,10,2,3,4,0,7,8,9,1]).reshape(-1,1)
y = np.array([130,21,43,76,105,3,167,162,91,15]).reshape(-1,1)
poly = skpepro.PolynomialFeatures(degree=8, include_bias=False).fit_transform(x)
model = skmodel.LinearRegression().fit(poly)
print(model.coef_)