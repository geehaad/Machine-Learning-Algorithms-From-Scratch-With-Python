import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn import datasets
matplotlib.pyplot as pyplot

X, y = datasets.make_regression(n_samples=100, n_features=1, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# fig = plt.figure(figsize=(8,6))
# plt.scatter(X[:,0], y, color ="b", marker = "x", s=30)

# plt.show()


# print(X_train.shape)
# print(y_train.shape)

import LinearRegression 

regressor = LinearRegression()
regressor.fit(X_train, y_train)

predicted = regressor.predict(X_test)


def mse(y_true, y_predicted):
    np.mean((y_true - y_predicted)**2)

mse_value = mse(y_test, predicted)
print(mse_value)