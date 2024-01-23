class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is not None:
            return self.head.data


class QueueLinkedList:
    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def enqueue(self, data):
        self.linked_list.insert_at_end(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        front_data = self.linked_list.peek()
        self.linked_list.delete_at_beginning()
        return front_data

    def is_empty(self):
        return self.linked_list.is_empty()

    def peek(self):
        return self.linked_list.peek()


class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, data):
        if self.is_full():
            raise IndexError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        front_data = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return front_data

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.array[self.front]


# Example usage
doubly_linked_list = DoublyLinkedList()

# Read numbers from file
with open('numbers-2.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

# Insert values
for value in values:
    doubly_linked_list.insert_at_end(value)

print("Original List:", doubly_linked_list.read())

doubly_linked_list.sort()
print("Sorted List:", doubly_linked_list.read())

# Create a Queue using Doubly Linked List
linked_list_queue = QueueLinkedList()

# Enqueue values into the linked list queue
for value in values:
    linked_list_queue.enqueue(value)

# Dequeue values from the linked list queue
print("Linked List Queue Dequeue:", linked_list_queue.dequeue())

# Check if the linked list queue is empty
print("Is Linked List Queue Empty?", linked_list_queue.is_empty())

# Peek at the front of the linked list queue
print("Linked List Queue Peek:", linked_list_queue.peek())

# Create a Queue using Array
array_queue = QueueArray(5)

# Enqueue values into the array queue
for value in values:
    array_queue.enqueue(value)

# Dequeue values from the array queue
print("Array Queue Dequeue:", array_queue.dequeue())

# Check if the array queue is empty
print("Is Array Queue Empty?", array_queue.is_empty())

# Peek at the front of the array queue
print("Array Queue Peek:", array_queue.peek())
