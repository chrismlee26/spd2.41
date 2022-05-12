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
# arr = [4, 6, 6, 6, 9], 
# key = 6

# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
def find_range_of_tree(tree1, target):
    if tree1.root is None:
        return [-1, -1]
    else:
        return find_range_of_tree_helper(tree1.root, target)

    
def find_range_of_tree_helper(node, target):
    if node is None:
        return [-1, -1]
    if node.v == target:
        return find_range_of_tree_helper(node.l, target)
    elif node.v < target:
        return find_range_of_tree_helper(node.r, target)
    else:
        return [node.v, node.v]

    
print("--------- Q1 ---------")
print(find_range_of_tree(tree1, 6))


# Examples
# input1 = [4, 6, 6, 6, 9] key1 = 6
# output1 = [1, 3]

# input2 = [1, 3, 8, 10, 15] key2 = 10
# output2 = [3, 3]

# input3 = [1, 3, 8, 10, 15] key3 = 12
# output3 = [-1, -1]


# Problem 2
# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing 
# or decreasing means that for any index i in the array arr[i] != arr[i+1].

# input = [1, 3, 8, 12, 4, 2]
# output = 12
# Explanation: The maximum number in the input bitonic array is '12'.
