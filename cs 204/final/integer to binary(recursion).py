def integer_to_binary(integer):
    if integer == 0:
        return ""
    else:
        return integer_to_binary(integer // 2) + str(integer % 2)

# Example
print(integer_to_binary(10))  # Output: 1010
