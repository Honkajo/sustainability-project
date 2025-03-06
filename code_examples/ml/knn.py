import random
import math

def this_func_knn(data, query, k):
    distances = []
    
    for i in range(len(data)):
        dist = 0
        for j in range(len(data[i])):
            dist += (data[i][j] - query[j]) ** 2
        dist = math.sqrt(dist)
        
        temp = [dist, i]
        distances.append(temp)
    
    distances_sorted = []
    for dist in distances:
        distances_sorted.append(dist[:])
    
    distances_sorted.sort(key=lambda x: x[0])
    
    nearest_neighbors = []
    for i in range(k):
        temp = distances_sorted[i][1]
        nearest_neighbors.append(temp)
    
    final_neighbors = []
    for neighbor in nearest_neighbors:
        final_neighbors.append(neighbor)
    
    return final_neighbors[:]

random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(3000000)]
query = [random.random() for _ in range(5)]
k = 3

this_func_knn(data, query, k)

