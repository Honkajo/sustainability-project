import random
import numpy as np

def efficient_kmeans(data, k, max_iters=100):
    data = np.array(data)
    centroids = data[np.random.choice(len(data), k, replace=False)]
    
    for _ in range(max_iters):
        # Assign points to the nearest centroid
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Update centroids
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
    
    return centroids

# Example usage
random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(100000)]
k = 3

centroids = efficient_kmeans(data, k)

