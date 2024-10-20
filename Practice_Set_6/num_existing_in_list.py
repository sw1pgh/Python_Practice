# WAP in Python to check whether an inputted number exists in the list or not

def does_number_exist():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    inputted_number = int(input("Please enter any number: "))  # Convert input to an integer

    if inputted_number in number_list:
        print("Your inputted number exists in our list!")
    else:
        print("Number does NOT exist in our list.")

if __name__ == "__main__":
    does_number_exist()