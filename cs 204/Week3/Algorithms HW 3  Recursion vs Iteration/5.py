def selection_sort_iterative(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Read a set of numbers from an external file
file_path = "numbers-3.txt"
with open(file_path, "r") as file:
    numbers = [int(line.strip()) for line in file]

# Sort the list using iterative selection sort
selection_sort_iterative(numbers)

# Target number to search for
target_number = 5842193

# Perform a binary search for the target number
index = binary_search_recursive(numbers, target_number, 0, len(numbers) - 1)

if index != -1:
    print(f"Target number {target_number} found at index {index}.")
else:
    print(f"Target number {target_number} not found in the sorted array.")

# Target number 8128705 found at index 8101.
# Target number 5842193 not found in the sorted array.