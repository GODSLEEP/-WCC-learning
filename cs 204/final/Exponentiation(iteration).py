def power(x, e):
    result = 1
    while e > 0:
        result *= x
        e -= 1
    return result

# Example usage
print(power(2, 3))  # Output: 8
