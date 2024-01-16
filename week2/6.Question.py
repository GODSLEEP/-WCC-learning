def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index is the minimum
        min_index = i
        
        # Find the index of the minimum element in the unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1     # Index of the last element in the sorted part

        # Compare key with elements in the sorted part, move greater elements to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key  # Insert key at the correct position in the sorted sequence

# Read numbers from file
with open('numbers-1.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Sort using selection sort
selection_sorted = numbers.copy()
selection_sort(selection_sorted)

# Sort using insertion sort
insertion_sorted = numbers.copy()
insertion_sort(insertion_sorted)

# Print the value at position 7586
print("Value at position 7586 (selection sort):", selection_sorted[7586])
print("Value at position 7586 (insertion sort):", insertion_sorted[7586])

# The value is in position 7586 is 7608064