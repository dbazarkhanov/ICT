import numpy as np
import sklearn.linear_model as skmod
import matplotlib.pyplot as plt

# x = np.array([25, 100, 30, 5, 85]).reshape(-1, 1)
# y = np.array([80, 254, 152, 4, 271]).reshape(-1, 1)

# plt.scatter(x, y)
# plt.show()

# model = skmod.LinearRegression()

# model_train = model.fit(x, y)

# print(model_train.coef_[0]*x + model_train.intercept_)
# plt.scatter(x, y)
# plt.show()

# model_train.fit_intercept(consider b=0 if False, default is True)

x1 = np.array([13,3,17,0,2]).reshape(-1, 1)
y = np.array([505,35,836,-6,16]).reshape(-1, 1)
x2 = x1**2
x = np.hstack([x1, x2])

model = skmod.LinearRegression().fit(x, y)

print(model.coef_)
print(model.intercept_)