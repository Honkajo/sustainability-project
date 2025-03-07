import random
import math

def knn(data, query, k):
    distances = [(math.sqrt(sum((data[i][j] - query[j]) ** 2 for j in range(len(query)))), i) for i in range(len(data))]
    distances.sort(key=lambda x: x[0])
    return [x[1] for x in distances[:k]]

random.seed(0)
data = [[random.random() for _ in range(5)] for _ in range(3000000)]
query = [random.random() for _ in range(5)]
k = 3

result = knn(data, query, k)

