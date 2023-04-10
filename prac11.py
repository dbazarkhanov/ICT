import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as skmod
import sklearn.preprocessing as skpepro
import sklearn.model_selection as sksel

df = pd.read_parquet('Data_to_analyse.parquet')
# print(df)

x1 = df['Age'].to_numpy().reshape(-1,1)
x2 = df['Account_money'].to_numpy().reshape(-1,1)
y = df['Money_given'].to_numpy().reshape(-1,1)

# plt.scatter(x1, y)
# plt.show()

# plt.scatter(x2, y)
# plt.show()

x12 = np.hstack([x1, x2])


x12_train, x12_test, y_train, y_test = sksel.train_test_split(x12, y, train_size=0.8)

# print(x12_test, x12_train, y_test, y_train)

scaler = skpepro.StandardScaler()
x12_scal_std = scaler.fit_transform(x12_train)

scaler_y = skpepro.StandardScaler()
y_scal_std = scaler_y.fit_transform(y_train)

# print(x12_scal_std, y_train)

model = skmod.LinearRegression().fit(x12_scal_std, y_scal_std)

# print(model.coef_)
# print(model.intercept_)
# print(model.score(x12_scal_std, y_scal_std))

# print('{:.2f}x1+{:.2f}x2+{:.2f}={:.2f}'.format(model.coef_[0][0], model.coef_[0][1], model.intercept_[0], model.score(x12_scal_std, y_scal_std)))

x12_scal_test_std = scaler.transform(x12_test)
y_scal_test_std = scaler_y.transform(y_test)

# print(model.score(x12_scal_std_test, y_scal_test))

predict = np.array([100_000, 20]).reshape(-1,1)
scaler = skpepro.StandardScaler()
predict_scal = scaler.fit_transform(predict)
print(predict_scal)