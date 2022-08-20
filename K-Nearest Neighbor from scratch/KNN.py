import numpy as  np
from collections import Counter

# Calculate all distances
# Check the label of the nearest labels
# Do a majority vote 
# Choose the most common class label

def euclidean(x1, x2):
    d = np.sqrt(np.sum((x1-x2)**2))
    return d

class KNN:

    # Parameter initialization 
    def __init__(self, k=3):
        self.k  = k

    # Train function, for KNN, this just memorize the data
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        

    # Test/ Predict function
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute the distances
        distances = [euclidean(x, x2) for x2 in self.X_train]

        # Get k nearest samples, labels
        k_indices = np.argsort(distances)[:self.k] # We need only the k nearest sample,
                                                  # So the slice will be untile the given k 
        k_nearest_labesl = [self.y_train[i] for i in k_indices] 

        # Majority vote, most common class label 
        most_common = Counter(k_nearest_labesl).most_common(1)
        return most_common[0][0]



    
    
    
    
