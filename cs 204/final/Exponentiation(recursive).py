def power(x, e):
    if e == 0:
        return 1
    else:
        return x * power(x, e - 1)

# Example
print(power(2, 3))  # Output: 8
