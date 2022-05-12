from LinkedList import LinkedList

# --------------------
# Question 1
# --------------------
# Example: If the given linked list is A → B → C → D → E, nodes should be modified/rearranged so the list becomes E → D → C → B → A.
regular_list = LinkedList()
regular_list.append('A')
regular_list.append('B')
regular_list.append('C')
regular_list.append('D')
regular_list.append('E')

def reverse_linked_list(linked_list):
    current = linked_list.head
    previous = None
    while current:
        next_node, current.next = current.next, previous
        previous, current = current, next_node
    linked_list.head = previous
    return linked_list

# print(reverse_linked_list(regular_list))

# --------------------
# Question 2
# --------------------
# 2. Given a singly-linked list, rearrange the nodes by interleaving the first half of the linked list with the second half.
# Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.
#nodes go from 1, 2, 3, 4, 5, 6, 7, 8 -> 1, 3, 5, 7, 2, 4, 6, 8

linkedlist = LinkedList()
linkedlist.append('A')
linkedlist.append('B')
linkedlist.append('C')
linkedlist.append('D')
linkedlist.append('E')
linkedlist.append('F')
linkedlist.append('G')
linkedlist.append('H')

def interleave_linked_list(linked_list):
    #If the given linked list is A → B → C → D → E → F → G → H, nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.
    # 1, 2, 3, 4, 5, 6, 7, 8 -> 1, 3, 5, 7, 2, 4, 6, 8
    odd = linked_list.head
    even = odd.next
    while even:
        odd.next = even.next
        even.next = odd
        odd = odd.next
        if odd:
            even = odd.next
        else:
            break
    linked_list.head = even
    return linked_list

# Can't get this one to work.
# print(interleave_linked_list(linkedlist))


# --------------------
# Question 3
# --------------------
# 3. Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.
# Example: If the given linked list is A → B → C → D → E → F and k is 4, nodes should be modified so the list becomes E → F → A → B → C → D.
# Assumptions: k is positive and smaller than n, the length of the linked list.

def rotate_linked_list(linkedlist, k):
    if k == 0:
        return

    current = linkedlist.head
    count = 1

    while(count <k and current is not None):
        current = current.next
        count += 1

    if current is None:
        return 

    kthNode = current

    while(current.next is not None):
        current = current.next

    current.next = linkedlist.head
    linkedlist.head = kthNode.next
    kthNode.next = None

    return linkedlist

print(rotate_linked_list(linkedlist, 4))


# --------------------
# Question 4
# --------------------
# 3. Given an array of k singly-linked lists, each of whose values are in sorted order, combine all nodes (do not create new nodes) into one singly-linked list with all values in order.


# --------------------
# Question 5
# --------------------
# 4. New: Given a singly-linked list and an integer k, find the value in the kth-to-last node.

