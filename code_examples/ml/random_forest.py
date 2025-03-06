import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import resample

def this_func(X, y, n_estimators=100):
    n_samples, n_features = X.shape
    trees = []

    for _ in range(n_estimators):
        indices = np.random.randint(0, n_samples, size=n_samples)
        X_bootstrap, y_bootstrap = X[indices], y[indices]

        tree = DecisionTreeClassifier(max_depth=5)
        tree.fit(X_bootstrap, y_bootstrap)
        trees.append(tree)

    predictions = np.zeros((n_samples, n_estimators))

    for i in range(n_samples):
        for j in range(n_estimators):
            predictions[i, j] = trees[j].predict([X[i]])

    final_predictions = []
    for i in range(n_samples):
        counts = np.bincount(predictions[i].astype(int))
        final_predictions.append(np.argmax(counts))

    return final_predictions


X = np.random.rand(1000, 5)
y = np.random.randint(0, 2, 1000)

predictions = this_func(X, y)
