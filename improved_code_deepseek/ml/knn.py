import random
import numpy as np

def efficient_knn(data, query, k):
    data = np.array(data)
    query = np.array(query)
    
    # Calculate Euclidean distances using vectorized operations
    distances = np.linalg.norm(data - query, axis=1)
    
    # Find the indices of the k smallest distances
    nearest_neighbors = np.argpartition(distances, k)[:k]
    
    return nearest_neighbors.tolist()

# Example usage
random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(3000000)]
query = [random.random() for _ in range(5)]
k = 3

nearest_neighbors = efficient_knn(data, query, k)

