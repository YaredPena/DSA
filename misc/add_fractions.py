def add_fractions(a, b, c, d):
    numerator = a * d + c * b
    denominator = b * d
    return (numerator, denominator)


# Example:
print(add_fractions(1, 3, 2, 5))  
