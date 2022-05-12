from LinkedList import LinkedList

# Example: If the given linked list is A → B → C → D → E, nodes should be modified/rearranged so the list becomes E → D → C → B → A.
regular_list = LinkedList()
regular_list.append('A')
regular_list.append('B')
regular_list.append('C')
regular_list.append('D')
regular_list.append('E')

# Example: If the given linked list is A → B → C → D → E, nodes should be modified/rearranged so the list becomes E → D → C → B → A.

def reverse_linked_list(linked_list):
    current = linked_list.head
    previous = None
    while current:
        next_node, current.next = current.next, previous
        previous, current = current, next_node
    linked_list.head = previous
    return linked_list

print(reverse_linked_list(regular_list))


# 1. Given a singly-linked list, rearrange the nodes by interleaving the first half of the linked list with the second half.
# Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.

# 2. Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.
# Example: If the given linked list is A → B → C → D → E → F and k is 4, nodes should be modified so the list becomes E → F → A → B → C → D.
# Assumptions: k is positive and smaller than n, the length of the linked list.

# 3. Given an array of k singly-linked lists, each of whose values are in sorted order, combine all nodes (do not create new nodes) into one singly-linked list with all values in order.

# 4. New: Given a singly-linked list and an integer k, find the value in the kth-to-last node.

