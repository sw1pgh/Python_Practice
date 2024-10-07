# Python program to take desired numbers as inputs in a list and then sum and print the value

def sum_numbers_in_list():
    limit = 0
    numbers = []

    limit = int(input("How many numbers do you want to inout for summation: "))

    for i in range(0, limit):
        number = int(input(f"Please enter the #{i+1} number: "))
        numbers.append(number)
    
    summation_value = sum(numbers)
    
    print(f"The Sum of the numbers is = {summation_value}")

if __name__ == "__main__":
    sum_numbers_in_list()