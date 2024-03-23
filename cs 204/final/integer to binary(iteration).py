def integer_to_binary(integer):
    binary_string = ""
    while integer > 0:
        remainder = integer % 2
        binary_string = str(remainder) + binary_string
        integer = integer // 2
    return binary_string

# Example
print(integer_to_binary(10))  # Output: 1010
