import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

def this_func(X, y, n_estimators=100):
    baggingclf = BaggingClassifier(DecisionTreeClassifier(max_depth=5), n_estimators=n_estimators)
    baggingclf.fit(X, y)
    return baggingclf.predict(X)

X = np.random.rand(1000, 5)
y = np.random.randint(0, 2, 1000)

predictions = this_func(X, y)

