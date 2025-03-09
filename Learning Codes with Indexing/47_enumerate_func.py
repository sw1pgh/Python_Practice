# Learning how to use enumerate function

list_LA = [1, 3, 2232, 32323, 99, 1, -19]

for item, i in enumerate(list_LA):
    print(f"The item at index {item} is {i}")
    print(list_LA[item])