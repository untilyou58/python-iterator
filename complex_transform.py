import itertools


def number_generator():
    for i in itertools.count(1):
        yield i


def square_numbers(numbers):
    for n in numbers:
        yield n**2


def even_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


# Build the lazy pipeline
numbers = number_generator()
squared_numbers = square_numbers(numbers)
even_squared_numbers = even_numbers(squared_numbers)

# Get the squared even numbers of the first 5 natural numbers
result = list(itertools.islice(even_squared_numbers, 5))
print(result)  # [4, 16, 36, 64, 100]

# Output:
# [4, 16, 36, 64, 100]
