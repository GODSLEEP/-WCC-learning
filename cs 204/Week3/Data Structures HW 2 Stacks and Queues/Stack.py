class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of bounds")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_at_position(self, position):
        if self.head is not None:
            if position == 0:
                self.head = self.head.next
            else:
                current = self.head
                for _ in range(position - 1):
                    if current is None or current.next is None:
                        raise IndexError("Position out of bounds")
                    current = current.next
                current.next = current.next.next

    def delete_at_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next.next is not None:
                    current = current.next
                current.next = None

    def linear_search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def read_from_beginning(self, k):
        elements = []
        current = self.head
        for _ in range(k):
            if current is not None:
                elements.append(current.data)
                current = current.next
        return elements

    def read_from_position(self, position, k):
        elements = []
        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        for _ in range(k):
            if current is not None:
                elements.append(current.data)
                current = current.next
        return elements

    def read_from_end(self, k):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements[-k:]

    def sort(self):
        # Using selection sort for simplicity
        current = self.head
        while current is not None:
            min_node = current
            runner = current.next
            while runner is not None:
                if runner.data < min_node.data:
                    min_node = runner
                runner = runner.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next


# Example usage
singly_linked_list = SinglyLinkedList()

# Read numbers from file
with open('numbers-2.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

# Insert values
for value in values:
    singly_linked_list.insert_at_end(value)

print("Original List:", singly_linked_list.read())

singly_linked_list.sort()
print("Sorted List:", singly_linked_list.read())

class StackLinkedList:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def push(self, data):
        self.linked_list.insert_at_end(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        last_node_data = self.linked_list.read_from_end(1)[0]
        self.linked_list.delete_at_end()
        return last_node_data

    def is_empty(self):
        return self.linked_list.head is None

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.linked_list.read_from_end(1)[0]


class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def push(self, data):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.array[self.top] = data

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        popped_data = self.array[self.top]
        self.top -= 1
        return popped_data

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.array[self.top]


# Example usage
linked_list_stack = StackLinkedList()
array_stack = StackArray(5)

# Push values onto the stacks
for value in values:
    linked_list_stack.push(value)
    array_stack.push(value)

# Pop values from the stacks
print("Linked List Stack Pop:", linked_list_stack.pop())
print("Array Stack Pop:", array_stack.pop())

# Check if stacks are empty
print("Is Linked List Stack Empty?", linked_list_stack.is_empty())
print("Is Array Stack Empty?", array_stack.is_empty())

# Peek at the top of the stacks
print("Linked List Stack Peek:", linked_list_stack.peek())
print("Array Stack Peek:", array_stack.peek())
