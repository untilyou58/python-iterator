# When working with large amounts of data,
# you can process it more efficiently by using an iterator rather than loading all the data into memory.


with open("large_file.txt", "r") as f:
    lines = (
        f.readlines()
    )  # Read all lines into a list - not recommended for large files
    for line in lines:
        print(len(line))

with open("large_file.txt", "r") as f:
    for line in f:  # Read line by line - recommended for large files
        print(len(line))
