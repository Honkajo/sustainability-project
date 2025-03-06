import random
import math

def this_func_kmeans(data, k, max_iters=100):
    centroids = random.sample(data, k)
    prev_centroids = [None] * k
    clusters = [[] for _ in range(k)]
    
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        
        for point in data:
            distances = []
            for centroid in centroids:
                dist = 0
                for i in range(len(centroid)):
                    dist += (point[i] - centroid[i]) ** 2
                distances.append(dist)
            
            min_distance_idx = distances.index(min(distances))
            clusters[min_distance_idx].append(point)
        
        prev_centroids = centroids[:]
        centroids = []
        
        for cluster in clusters:
            if cluster:
                centroid = [0] * len(cluster[0])
                for point in cluster:
                    for i in range(len(centroid)):
                        centroid[i] += point[i]
                centroid = [x / len(cluster) for x in centroid]
                centroids.append(centroid)
            else:
                centroids.append(prev_centroids[clusters.index(cluster)])
    
    return centroids

random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(100000)]
k = 3

this_func_kmeans(data, k)
