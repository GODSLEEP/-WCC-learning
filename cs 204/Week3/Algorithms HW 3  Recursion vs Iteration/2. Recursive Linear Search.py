# Recursive Linear Search
def linear_search_recursive(array, target, index=0):
    if index == len(array):
        return -1  # Target not found
    elif array[index] == target:
        return index
    else:
        return linear_search_recursive(array, target, index + 1)
