# This is the original code for selection sort
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

# This is the recursive way
def selection_sort_recursive(arr, i=0):
    n = len(arr)

    # Base case: If the entire array is sorted
    if i == n - 1:
        return

    # Find the index of the minimum element in the unsorted part
    min_index = find_min_index(arr, i, i + 1, n)

    # Swap the found minimum element with the first unsorted element
    arr[i], arr[min_index] = arr[min_index], arr[i]

    # Recursively sort the remaining unsorted part
    selection_sort_recursive(arr, i + 1)

def find_min_index(arr, min_index, j, n):
    # Base case: If we have checked the entire unsorted part
    if j == n:
        return min_index

    # Update min_index if a smaller element is found
    if arr[j] < arr[min_index]:
        min_index = j

    # Recursively find the minimum index in the rest of the unsorted part
    return find_min_index(arr, min_index, j + 1, n)

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort_recursive(arr)
print("Sorted array:", arr)
