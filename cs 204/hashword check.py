import hashlib

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # Insert a new node with data at the end of the linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target):
        # Search for a target value in the linked list
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, word):
        # Hash function using SHA-256 for the word, mapping it to an index in the table
        return int(hashlib.sha256(word.encode()).hexdigest(), 16) % self.size

    def insert(self, word):
        # Insert a word into the hash table
        index = self.hash_function(word)
        self.table[index].insert_at_end(word)

    def search(self, word):
        # Search for a word in the hash table
        index = self.hash_function(word)
        return self.table[index].search(word)

def levenshtein_distance(word1, word2):
    # Calculate the Levenshtein distance between two words
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)

    cost = 0 if word1[-1] == word2[-1] else 1

    delete = levenshtein_distance(word1[:-1], word2) + 1
    insert = levenshtein_distance(word1, word2[:-1]) + 1
    substitute = levenshtein_distance(word1[:-1], word2[:-1]) + cost

    return min(delete, insert, substitute)

def suggest_corrections(dictionary, misspelled_word):
    # Provide suggestions for corrections based on Levenshtein distance
    suggestions = []
    for word in dictionary:
        distance = levenshtein_distance(misspelled_word, word)
        if distance <= 2:  # Allow words with edit distance <= 2 as suggestions
            suggestions.append(word)
    return suggestions

def main():
    dictionary_file = "dictionary.txt"
    hash_table_size = 1000

    # Load dictionary into hash table
    hash_table = HashTable(hash_table_size)
    with open(dictionary_file, "r") as file:
        for line in file:
            word = line.strip()
            hash_table.insert(word)

    while True:
        user_input = input("Enter text (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        words = user_input.split()
        misspelled_words = []

        for word in words:
            if not hash_table.search(word):
                print(f"Misspelled: {word}")
                suggestions = suggest_corrections(hash_table, word)
                if suggestions:
                    print(f"Suggestions: {', '.join(suggestions)}")
                misspelled_words.append(word)

        if misspelled_words:
            add_to_dictionary = input("Do you want to add words to the dictionary? (yes/no): ")
            if add_to_dictionary.lower() == "yes":
                for misspelled_word in misspelled_words:
                    hash_table.insert(misspelled_word)
                    print(f"Added '{misspelled_word}' to the dictionary.")

if __name__ == "__main__":
    main()
