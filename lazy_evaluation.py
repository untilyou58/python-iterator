# Normal function (keeps all values in memory)
def get_squares(n):  # n is the number of squares to generate -> n = 1000000
    return [x**2 for x in range(n)]


# for square in get_squares(100000000):
#     if square > 100:
#         break
#     print(square)


# Generator functions (generate values as needed)
def get_squares_generator(n):
    for x in range(n):
        yield x**2


# examples showing the use (of a word)
for square in get_squares_generator(100000000):
    if square > 100:
        break
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
