# Challenging problems we’ve seen before:

#1.  Given an array of k singly-linked lists, each of whose values are in sorted order, combine all nodes (do not create new nodes) into one singly-linked list with all values in order.
# --------------------
# Question 1
# --------------------


# Maybe next time you want to assign linked list and bst problems to someone else you should at least have the courtesy to write the code for it. 


# Linked List Node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Linked List Code:
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.length -= 1
                return True
            previous = current
            current = current.next
        return False
    def __len__(self):
        return self.length
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)
    def __repr__(self):
        return self.__str__()
    def __iter__(self):
        self.current = self.head
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value
    # append
    def append(self, value):
      new_node = Node(value)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        self.tail = new_node
      self.length += 1
    # insert
    def insert(self, index, value):
      if index < 0 or index > self.length:
        raise IndexError
      if index == 0:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
      else:
        current = self.head
        previous = None
        for i in range(index):
          previous = current
          current = current.next
        new_node = Node(value)
        new_node.next = current
        previous.next = new_node
      self.length += 1

  

# Example singly linked list 1:
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

list2 = LinkedList()
list2.append(4)
list2.append(5)
list2.append(6)

def combine_sorted_linked_lists(list1, list2):
    # create a new list to store the combined lists
    combined_list = LinkedList()
    # create a pointer to the first node of the first list
    first_list = list1.head
    # create a pointer to the first node of the second list
    second_list = list2.head
    # while there are still nodes in the first list
    while first_list:
        # add the first node of the first list to the combined list
        combined_list.append(first_list.value)
        # move the first list pointer to the next node
        first_list = first_list.next
    # while there are still nodes in the second list
    while second_list:
        # add the first node of the second list to the combined list
        combined_list.append(second_list.value)
        # move the second list pointer to the next node
        second_list = second_list.next
    # return the combined list
    return combined_list

print(combine_sorted_linked_lists(list1, list2))

#2.  Given a binary search tree, convert it into a sorted doubly-linked list by modifying the original tree nodes (do not create new nodes).
# --------------------
# Question 2
# --------------------

def convert_bst_to_sorted_doubly_linked_list(tree):
    # create a new list to store the sorted list
    sorted_list = LinkedList()
    # create a pointer to the root node of the tree
    current = tree.root
    # while the current node is not None
    while current:
        # add the current node to the sorted list
        sorted_list.append(current.value)
        # move the current node to the left child
        current = current.left
    # return the sorted list
    return sorted_list


#3.  Let’s say a binary tree is "super balanced" if the difference between the depths of any two leaf nodes is at most one. Write a function to check if a binary tree is "super balanced".
# --------------------
# Question 3
# --------------------

def is_it_super_balanced(tree):
    # create a stack to store the nodes
    stack = []
    # create a variable to store the depth of the current node
    current_depth = 0
    # create a variable to store the depth of the deepest node
    deepest_depth = 0
    # create a variable to store the difference between the depths of the deepest node and the current node
    difference = 0
    # create a variable to store the result of the function
    result = True
    # create a pointer to the root node of the tree
    current = tree.root
    # while the current node is not None
    while current:
        # if the current node has a left child
        if current.left:
            # add the current node to the stack
            stack.append(current)
            # move the current node to the left child
            current = current.left
            # increase the depth of the current node
            current_depth += 1
        # if the current node has no left child
        else:
            # if the current node has a right child
            if current.right:
                # add the current node to the stack
                stack.append(current)
                # move the current node to the right child
                current = current.right
                # increase the depth of the current node
                current_depth += 1
            # if the current node has no right child
            else:
                # if the stack is not empty
                if stack:
                    # pop the last node from the stack
                    current = stack.pop()
                    # decrease the depth of the current node
                    current_depth -= 1
                # if the stack is empty
                else:
                    # set the deepest depth to the current depth
                    deepest_depth = current_depth
                    # set the current depth to 0
                    current_depth = 0
                    # set the current node to None
                    current = None
    # set the difference between the depths of the deepest node and the current node
    difference = deepest_depth - current_depth
    # if the difference is greater than 1
    if difference > 1:
        # set the result to False
        result = False
    # return the result
    return result
