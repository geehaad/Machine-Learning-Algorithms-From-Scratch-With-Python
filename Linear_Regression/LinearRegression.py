import numpy as np 

class LinearRegression: 

    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = 0

    def fit(self, X, y):

        #init parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) + np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) + np.sum(X.T, (y_predicted - y))

            self.weights -= self.lr * dw 
            self.bias -= seld.lr * db


    def predict(self, X):
         y_predicted = np.dot(X, self.weights) + self.bias
         return y_predicted 