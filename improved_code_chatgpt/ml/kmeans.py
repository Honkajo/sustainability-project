import random
import numpy as np

def this_func_kmeans(data, k, max_iters=100):
    # Convert the data to a numpy array for vectorized operations
    data = np.array(data)
    
    # Initialize centroids randomly
    centroids = data[random.sample(range(len(data)), k)]
    
    # Store previous centroids for convergence check
    prev_centroids = np.zeros_like(centroids)
    
    for _ in range(max_iters):
        # Create empty clusters
        clusters = [[] for _ in range(k)]
        
        # Assign points to the nearest centroid
        for point in data:
            distances = np.linalg.norm(centroids - point, axis=1)  # Vectorized distance calculation
            min_distance_idx = np.argmin(distances)
            clusters[min_distance_idx].append(point)
        
        # Store previous centroids
        prev_centroids = centroids.copy()
        
        # Update centroids
        for i, cluster in enumerate(clusters):
            if cluster:
                centroids[i] = np.mean(cluster, axis=0)
            else:
                # In case of empty cluster, choose a random point
                centroids[i] = random.choice(data)
        
        # Convergence check: if centroids do not change, break early
        if np.allclose(centroids, prev_centroids):
            break
    
    return centroids

# Example usage
random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(100000)]
k = 3

centroids = this_func_kmeans(data, k)
print(centroids)

