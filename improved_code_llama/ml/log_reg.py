import numpy as np

def logistic_regression(X, y, learning_rate=0.01, epochs=100):
    m, n = X.shape
    weights = np.random.rand(n)
    bias = 0

    for _ in range(epochs):
        predictions = np.dot(X, weights) + bias
        predictions = 1 / (1 + np.exp(-predictions))
        errors = y - predictions
        weights += learning_rate * np.dot(X.T, errors)
        bias += learning_rate * np.sum(errors)

    return weights, bias

# Example usage
X = np.random.rand(10000, 5)  # 100 samples, 3 features
y = np.random.randint(0, 2, 10000)  # Binary target

weights, bias = logistic_regression(X, y)

