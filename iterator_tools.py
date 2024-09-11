import itertools


# Condition for unlimited loop
for i in itertools.count(1):
    if i > 5:
        break
    print(i)  # 1, 2, 3, 4, 5

# Output:
# 1
# 2
# 3
# 4
# 5

# Looping through two lists simultaneously
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
for item in itertools.product(colors, sizes):
    print(item)  # ('red', 'S'), ('red', 'M'), ...

# Output:
# ('red', 'S')
# ('red', 'M')
# ('red', 'L')
# ('green', 'S')
# ('green', 'M')
# ('green', 'L')
# ('blue', 'S')
# ('blue', 'M')
# ('blue', 'L')

# Looping through a list with an index
data = [1, 1, 2, 3, 3, 3, 4, 5, 5]
for key, group in itertools.groupby(data):
    print(key, list(group))  # 1 [1, 1], 2 [2], 3 [3, 3, 3], ...

# Output:
# 1 [1, 1]
# 2 [2]
# 3 [3, 3, 3]
# 4 [4]
# 5 [5, 5]
