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

print("--------- Q1 ---------")
print(reverse_linked_list(regular_list))
print("\n")

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
# print("--------- Q2 ---------")
# print(interleave_linked_list(linkedlist))
# print('\n')


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

print("--------- Q3 ---------")
print(rotate_linked_list(linkedlist, 4))
print('\n')


# --------------------
# Question 4
# --------------------

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)

ll2 = LinkedList()
ll2.append(4)
ll2.append(5)
ll2.append(6)

ll3 = LinkedList()
ll3.append(7)
ll3.append(8)
ll3.append(9)

# 4. Given an array of k singly-linked lists, each of whose values are in sorted order, combine all nodes (do not create new nodes) into one singly-linked list with all values in order.
# Combine a list of sorted linked lists into one sorted linked list.
def combine_linked_lists(linked_lists):
    if len(linked_lists) == 0:
        return
    if len(linked_lists) == 1:
        return linked_lists[0]
    if len(linked_lists) == 2:
        return linked_lists[0].merge(linked_lists[1])
    else:
        return linked_lists[0].merge(combine_linked_lists(linked_lists[1:]))

print("--------- Q4 ---------")
print(combine_linked_lists([ll1, ll2, ll3]))
print('\n')

# --------------------
# Question 5
# --------------------
# 5. New: Given a singly-linked list and an integer k, find the value in the kth-to-last node.

def print_kth_to_last(linked_list, k):
    current = linked_list.head

    length = 0
    while current:
        length += 1
        current = current.next

    if k > length:
        return 
    current = linked_list.head
    for i in range(0, length - k):
        current = current.next
    return current.value

print("--------- Q5 ---------")
print(print_kth_to_last(ll3, 2))
