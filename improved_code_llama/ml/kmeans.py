import random
import math

def kmeans(data, k, max_iters=100):
    centroids = random.sample(data, k)
    clusters = [[] for _ in range(k)]
    
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        
        for point in data:
            min_distance_idx = -1
            min_distance = float('inf')
            for i, centroid in enumerate(centroids):
                distance = sum((point[j] - centroid[j]) ** 2 for j in range(len(point)))
                if distance < min_distance:
                    min_distance = distance
                    min_distance_idx = i
            clusters[min_distance_idx].append(point)
        
        new_centroids = []
        for cluster in clusters:
            if cluster:
                centroid = [sum(point[j] for point in cluster) / len(cluster) for j in range(len(cluster[0]))]
                new_centroids.append(centroid)
            else:
                new_centroids.append(centroids[clusters.index(cluster)])
        centroids = new_centroids
    
    return centroids

random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(100000)]
k = 3

result = kmeans(data, k)

