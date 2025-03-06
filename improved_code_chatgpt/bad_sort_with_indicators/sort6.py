import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Efficient function to insert elements into a BST
def efficient_insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = efficient_insert(root.left, value)
    else:
        root.right = efficient_insert(root.right, value)
    return root

# Efficient in-order traversal
def efficient_inorder_traversal(root):
    if root is None:
        return []
    return efficient_inorder_traversal(root.left) + [root.value] + efficient_inorder_traversal(root.right)

# Efficient Tree Sort function
def efficient_tree_sort(arr):
    if not arr:
        return arr

    root = None
    for num in arr:
        root = efficient_insert(root, num)

    return efficient_inorder_traversal(root)

random.seed(0)
L_size = 600000  # Adjust the size of the list
L = [random.random() for _ in range(L_size)]  # Efficient list initialization

sorted_list = efficient_tree_sort(L)

