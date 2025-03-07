import numpy as np

def efficient_computation(vector1, vector2):
    # Convert lists to NumPy arrays
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    
    # Perform the computation using NumPy
    result = vector1[:, np.newaxis] * vector2 - vector1[:, np.newaxis] * vector2
    
    return result

# Example usage
random.seed(0)
L_size = 6000  # int to pass to range
L = [random.random() for _ in range(L_size)]
L2 = [random.random() for _ in range(L_size)]

result = efficient_computation(L, L2)

