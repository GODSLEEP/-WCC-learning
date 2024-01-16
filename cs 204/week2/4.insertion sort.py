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

# Example usage
my_array = [64, 25, 12, 22, 11]
insertion_sort(my_array)

print("Sorted array:", my_array)