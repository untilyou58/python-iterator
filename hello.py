def main():
    my_list = [1, 2, 3]
    my_tuple = (4, 5, 6)
    my_string = "Hello"
    my_dict = {"a": 1, "b": 2}
    my_set = {7, 8, 9}

    # for loop
    for item in my_list:
        print(item)

    # result:
    # 1
    # 2
    # 3

    # for loop
    print(list(my_tuple))
    print(list(my_string))
    print(list(my_dict))
    print(list(my_set))

    # Iter in Python
    my_list = [1, 2, 3]
    my_iterator = iter(my_list)

    print(next(my_iterator))  # 1
    print(next(my_iterator))  # 2
    print(next(my_iterator))  # 3


if __name__ == "__main__":
    main()
