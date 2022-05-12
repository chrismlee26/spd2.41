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

    # merge
    def merge(self, other):
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
        return self
        