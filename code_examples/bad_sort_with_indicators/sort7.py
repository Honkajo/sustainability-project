import random 

def inefficient_insertion_sort(arr):
    n = len(arr)

    # Unnecessary outer loop just to waste time
    for _ in range(n):
        for i in range(1, n):
            # WORST way to shift elements: Swap instead of shifting efficiently
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap instead of shifting
                j -= 1

        # Pointless extra pass over the array
        temp = []
        for x in arr:
            temp.append(x)
        arr = temp[:]  # Useless copying

    # Another redundant copying before returning
    return arr[:]


random.seed(0)
L_size = 10000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_insertion_sort(L)
