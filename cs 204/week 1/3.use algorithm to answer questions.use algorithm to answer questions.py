# open file and read the content into the array
with open('numbers.txt', 'r') as file: # O(1)
    lines = file.readlines() #O(n) n is the number of lines in the file
    example = [int(line.strip()) for line in lines] #O(n) n is the number of lines in the file

# make array in the right order
# example.sort() I don't know maybe O(n log n)

# set the target
target = 196614208 #O(1)

# binary search function
def binary_search(arr, target): #O(log n) n is the size of array
    left = 0
    right = len(arr) - 1
    operations = 0  # Initialize the counter for operations

    while left <= right:
        mid = (left + right) // 2
        operations += 1
        if arr[mid] == target:
            return mid, operations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, operations

# start binary search
result, operations = binary_search(example, target)# O(log n) Invoking the binary search function to find the target value

# show the result and times of operations
print(result) # O(1) printing the result has a constant-time complexity
print(operations)# O(1) printing the result has a constant-time complexity

def overall_time_complexity(n):
    return f"O(n) + O(log n)"

print(overall_time_complexity(n))