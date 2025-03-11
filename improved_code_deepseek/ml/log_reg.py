import numpy as np

def efficient_logistic_regression(X, y, learning_rate=0.01, epochs=100):
    m, n = X.shape
    weights = np.random.rand(n)
    bias = 0

    for _ in range(epochs):
        # Vectorized computation of predictions
        linear_model = np.dot(X, weights) + bias
        predictions = 1 / (1 + np.exp(-linear_model))

        # Vectorized computation of errors
        errors = y - predictions

        # Vectorized updates for weights and bias
        weights += learning_rate * np.dot(X.T, errors) / m
        bias += learning_rate * np.sum(errors) / m

    return weights, bias

# Example usage
X = np.random.rand(10000, 5)  # 10000 samples, 5 features
y = np.random.randint(0, 2, 10000)  # Binary target

weights, bias = efficient_logistic_regression(X, y)

