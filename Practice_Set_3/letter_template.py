# Fill in a letter template with below name and date
from datetime import datetime

def name_input():
    while True:
        input_name = input("Please enter your name: ").strip()
        if not input_name:  # Check for empty input
            print("Name cannot be empty. Please enter a valid name.")
        elif not all(char.isalpha() or char.isspace() for char in input_name):  # Check for valid characters
            print("Name can only contain letters and spaces. Please enter a valid name.")
        else:
            return input_name

def get_current_date(format_string="%d/%m/%Y"):
    return datetime.now().strftime(format_string)

def letter_format():
    print(f"Dear {name_input()},\nYou are Selected!\n{get_current_date()}\n")

if __name__ == "__main__":
    letter_format()