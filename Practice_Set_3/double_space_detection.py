# Program to detect double spaces in a string

def name_input():
    return input("Please enter any string: ")

def double_space_count(input_string):
    counter = 0
    counter = input_string.count("  ")
    return counter

def replace_double_with_single(input_string):
    new_string = input_string.replace("  ", " ")
    return new_string

if __name__ == "__main__":
    input_string = name_input()
    print(f"Double Spaces = {double_space_count(input_string)}")
    print(f"After removing the double spaces, we got: {replace_double_with_single(input_string)}")