# List comprehension is a concise way to create lists in Python.
squares = [x**2 for x in range(10)]
print(squares)

# Output:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expressions are similar to list comprehensions, but they generate values one at a time.
even_squares = (x**2 for x in range(10) if x % 2 == 0)

# Usage example:
print(sum(even_squares))  # Sum of even squares from 0 to 9

# Output:
# 220
