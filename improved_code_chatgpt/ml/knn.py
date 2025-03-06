import random
import math
import numpy as np
import heapq

def this_func_knn(data, query, k):
    # Convert data and query to numpy arrays for efficient computation
    data = np.array(data)
    query = np.array(query)
    
    # Compute the Euclidean distance using numpy (vectorized operation)
    distances = np.linalg.norm(data - query, axis=1)
    
    # Use a heap to get the indices of the k smallest distances
    nearest_neighbors = heapq.nsmallest(k, range(len(distances)), key=lambda i: distances[i])
    
    return nearest_neighbors

# Example usage:
random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(3000000)]
query = [random.random() for _ in range(5)]
k = 3

neighbors = this_func_knn(data, query, k)
neighbors

