# Iterative Linear Search
def linear_search_iterative(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1  # Target not found
