import numpy as np
import sklearn.linear_model as skmod
import matplotlib.pyplot as plt

x1 = np.array([6,10,2,3,4,0,7,8,9,1]).reshape(-1,1)
y = np.array([130,21,43,76,105,3,167,162,91,15]).reshape(-1,1)
x2 = x1**2
x3 = x1**3

#print(x1, x2, x3, y, sep='\n')

model = skmod.LinearRegression().fit(x1,y)

# print(model.coef_)
# print(model.intercept_)
# print(model.score(x1, y))

x12 = np.hstack([x1, x2])
x123 = np.hstack([x1, x2, x3])

model_x2 = skmod.LinearRegression().fit(x12,y)
model_x3 = skmod.LinearRegression().fit(x123,y)

# print('{:.2f}x+{:.2f}={:.2f}'.format(model.coef_[0][0], model.intercept_[0], model.score(x1,y)))
# print('{:.2f}x{:.2f}x^2{:.2f}={:.2f}'.format(
#     model_x2.coef_[0][0], model_x2.coef_[0][1], model_x2.intercept_[0], model_x2.score(x12,y)))
# print('{:.2f}x+{:.2f}x^2{:.2f}x^3+{:.2f}={:.2f}'.format(
#     model_x3.coef_[0][0], model_x3.coef_[0][1], model_x3.coef_[0][2], model_x3.intercept_[0], model_x3.score(x123,y)))

plt.scatter(x1, y)
plt.plot([0,10], model.predict(np.array([[0],[10]])))
x_for_plot = np.arrange(0, 10, 0.1).reshape(-1, 1)
x2_for_plot = x_for_plot**2
plt.plot(x_for_plot, model.predict(np.hstack(x_for_plot,x2_for_plot)))
plt.show()