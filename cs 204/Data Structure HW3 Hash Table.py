class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def display(self):
        for i in range(self.size):
            print(f"Slot {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")

# Example usage:
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("orange", 15)

print("After insertion:")
hash_table.display()

print("\nSearch for 'banana':", hash_table.search("banana"))
print("Search for 'grape':", hash_table.search("grape"))

hash_table.delete("banana")

print("\nAfter deletion:")
hash_table.display()
