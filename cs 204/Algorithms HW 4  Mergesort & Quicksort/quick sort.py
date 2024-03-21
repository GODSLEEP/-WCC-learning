def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

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
        quick_sort(numbers, 0, len(numbers) - 1)
        position = find_position(numbers, num)
        if position != -1:
            print(f"The position of {num} in the sorted array is: {position + 1}")
        else:
            print(f"{num} is not found in the file.")

filename = "numbers-4.txt"
num_to_find = 90262
sort_and_find_position(filename, num_to_find)
# 90262 is in 3609 
# 11559 is not in the file