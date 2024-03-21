def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def find_position(arr, num):
    # Using binary search to find the position of num in the sorted array
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def sort_and_find_position(filename, num):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        merge_sort(numbers)
        position = find_position(numbers, num)
        if position != -1:
            print(f"The position of {num} in the sorted array is: {position + 1}")
        else:
            print(f"{num} is not found in the file.")

filename = "numbers-4.txt"
num_to_find = 11559
sort_and_find_position(filename, num_to_find)
# 90262 is in 3609 
# 11559 is not in the file
