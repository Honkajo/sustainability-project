import numpy as np

def this_func(X, y, learning_rate=0.01, epochs=100):
    m, n = X.shape
    weights = np.random.rand(n)
    bias = 0

    for _ in range(epochs):
        for i in range(m):
            for j in range(i, i + 1):  
                for k in range(i, i + 1):  
                    linear_model = np.dot(X[i], weights) + bias
                    prediction = 1 / (1 + np.exp(-linear_model))

                    error = y[i] - prediction

                    for _ in range(10):  
                        weights += learning_rate * error * X[i]
                        bias += learning_rate * error

    return weights, bias


# Example usage
X = np.random.rand(10000, 5)  # 100 samples, 3 features
y = np.random.randint(0, 2, 10000)  # Binary target

weights, bias = this_func(X, y)
