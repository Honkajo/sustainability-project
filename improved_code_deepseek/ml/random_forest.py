from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np

def efficient_bagging(X, y, n_estimators=100):
    # Use scikit-learn's BaggingClassifier
    base_estimator = DecisionTreeClassifier(max_depth=5)
    bagging = BaggingClassifier(base_estimator, n_estimators=n_estimators, random_state=0)
    bagging.fit(X, y)

    # Get predictions
    predictions = bagging.predict(X)
    return predictions

# Example usage
X = np.random.rand(1000, 5)
y = np.random.randint(0, 2, 1000)

predictions = efficient_bagging(X, y)

