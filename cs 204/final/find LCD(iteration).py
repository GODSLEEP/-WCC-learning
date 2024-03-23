def find_lcd(numerator, denominator):
    while denominator != 0:
        temp = denominator
        denominator = numerator % denominator
        numerator = temp
    return numerator

# Example
print(find_lcd(12, 18))  # Output: 6
