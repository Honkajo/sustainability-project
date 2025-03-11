import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if root.value > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def tree_sort(arr):
    if not arr:
        return arr
    root = None
    for num in arr:
        root = insert(root, num)
    return inorder_traversal(root)

random.seed(0)
L_size = 600000 
L = [random.random() for _ in range(L_size)]

result = tree_sort(L)

