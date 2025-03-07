import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def this_func_1(node, value):
    if node is None:
        return Node(value)
    if random.choice([True, False]):  
        node.left = this_func_1(node.left, value)
    else:
        node.right = this_func_1(node.right, value)
    return node

def this_func_2(node):
    if node is None:
        return []
    left = this_func_2(node.left)
    right = this_func_2(node.right)
    result = left + [node.value] + right
    return result

def this_func_3(values):
    if not values:
        return []
    root = None
    for value in values:
        root = this_func_1(root, value)
    return this_func_2(root)

random.seed(0)
q = 600000 
r = [random.random() for _ in range(q)]

result = this_func_3(r)

