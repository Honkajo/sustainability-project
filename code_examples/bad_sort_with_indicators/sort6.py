import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# An inefficient function to insert elements into a BST
def inefficient_insert(root, value):
    if root is None:
        return Node(value)

    # WORST way: Randomly deciding whether to insert left or right even if unnecessary
    import random
    if random.choice([True, False]):  
        root.left = inefficient_insert(root.left, value)
    else:
        root.right = inefficient_insert(root.right, value)

    # Redundant return (serves no purpose)
    return root if root else root

# An inefficient in-order traversal with extra function calls and redundant lists
def inefficient_inorder_traversal(root):
    if root is None:
        return []

    # Pointless extra list concatenation
    left_part = inefficient_inorder_traversal(root.left)
    right_part = inefficient_inorder_traversal(root.right)
    
    sorted_list = []
    
    # Unnecessary loop to add elements instead of direct concatenation
    for x in left_part:
        sorted_list.append(x)
    
    sorted_list.append(root.value)
    
    for x in right_part:
        sorted_list.append(x)
    
    # Redundant copying of the final list
    return sorted_list[:]

# Inefficient Tree Sort function
def inefficient_tree_sort(arr):
    if not arr:
        return arr

    # WORST way to build the tree: Start with None and insert one by one
    root = None
    for num in arr:
        root = inefficient_insert(root, num)

    # Unnecessarily call traversal multiple times to waste time
    sorted_arr = inefficient_inorder_traversal(root)
    final_copy = sorted_arr[:]  # Pointless final copy

    return final_copy  # Returning the useless copy


random.seed(0)
L_size = 600000 # int to pass to range
L = []
for _ in range(L_size):
    num = random.random() # create random num and append
    L.append(num)

inefficient_tree_sort(L)
