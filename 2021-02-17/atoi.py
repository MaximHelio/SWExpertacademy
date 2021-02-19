def atoi(num_str):
    value = 0

    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')
        print(value)
    return value

num_str = "1234"

num_int = atoi(num_str)
print(num_int, type(num_int))