class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_position(self, position, data):
        new_node = DoublyNode(data)
        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of bounds")
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

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

    def delete_at_position(self, position):
        if self.head is not None:
            if position == 0:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
            else:
                current = self.head
                for _ in range(position):
                    if current is None:
                        raise IndexError("Position out of bounds")
                    current = current.next
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev

    def delete_at_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                if current.prev is not None:
                    current.prev.next = None

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
