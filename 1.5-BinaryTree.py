from BinaryTree import BinaryTree

# Binary Search Tree Problems

# Problem 1
# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
# Input: 
tree1 = BinaryTree()
tree1.add(4)
tree1.add(6)
tree1.add(6)
tree1.add(6)
tree1.add(9)
tree1.printTree()
arr = [4, 6, 6, 6, 9] 
# key = 6

def find_indexes(arr, target):
    if len(arr) == 0:
        return (-1, -1)
    if arr[0] == target:
        return 0
    # Find all instances of target
    indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)
    # Return first and last instance of target
    if len(indexes) == 0:
        return (-1, -1)
    return (indexes[0], indexes[-1])

print("--------- Q1 ---------")
print(find_indexes(arr, 6))
print(find_indexes(arr, 3))
print("\n")


# Problem 2
# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing 
# or decreasing means that for any index i in the array arr[i] != arr[i+1].
# Write a function to find the maximum value in a given Bitonic array.
def find_max_bitonic(arr):
    arr.sort()
    return arr[-1]


# Explanation: The maximum number in the input bitonic array is '12'.
input = [1, 3, 8, 12, 4, 2]
# output = 12

print("--------- Q1 ---------")
print(find_max_bitonic(input))


# Problem 3
# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

def reverse_bst(node):
    if node is None:
        return None
    
    node.left, node.right = node.right, node.left
    
    reverse_bst(node.left)
    reverse_bst(node.right)

    return node

# Problem 4
# Given a binary search tree containing integers and a target integer, come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.

def find_sum_bst(node, target):
    if node is None:
        return None
    
    if node.data == target:
        return node
    
    left = find_sum_bst(node.left, target - node.data)
    right = find_sum_bst(node.right, target - node.data)
    
    if left is not None:
        return left
    return right

# Problem 5 
# Given a binary tree containing numbers, find the maximum sum path (the path that has the largest sum of node values). The path may start and end at any node in the tree.

def find_max_path(node):
    if node is None:
        return 0
    
    left = find_max_path(node.left)
    right = find_max_path(node.right)
    
    return max(left, right) + node.data
