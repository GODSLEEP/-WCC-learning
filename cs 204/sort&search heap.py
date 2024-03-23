import heapq

class SearchAndSortHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def search(self, value):
        return value in self.heap

    def sort(self):
        sorted_values = []
        while self.heap:
            sorted_values.append(heapq.heappop(self.heap))
        return sorted_values

# Example:
heap_instance = SearchAndSortHeap()

# Insert elements into the heap
elements_to_insert = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for element in elements_to_insert:
    heap_instance.insert(element)

# Search for an element
element_to_search = 4
if heap_instance.search(element_to_search):
    print(f"{element_to_search} found in the heap.")
else:
    print(f"{element_to_search} not found in the heap.")

# Sort the heap
sorted_heap = heap_instance.sort()
print("Sorted Heap:", sorted_heap)
