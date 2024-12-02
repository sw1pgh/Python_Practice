# Write the same good day program in python using function but this time provide the name as teh function parameter.

def good_day(name):
    print(f"Good Day {name}")


def name_input():
    input_name = input("Please enter your name: ")
    good_day(input_name)
    
if __name__ == "__main__":
    name_input()