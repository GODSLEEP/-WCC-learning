def find_lcd(numerator, denominator):
    if denominator == 0:
        return numerator
    else:
        return find_lcd(denominator, numerator % denominator)

# Example
print(find_lcd(12, 18))  # Output: 6
