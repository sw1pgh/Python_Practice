# Program to enter 4 nos from the user and find the greatest number

class Greatest_Number:
    def greatest(self):
        list_nos = []
        for i in range(4):
            number = int(input(f"Please enter the #{i+1} number: "))
            list_nos.append(number)

        greatest_num = list_nos[0]  # Initialize with the first number
        for num in list_nos:
            if num > greatest_num:
                greatest_num = num

        return greatest_num

if __name__ == "__main__":
    result = Greatest_Number().greatest()
    print(f"The greatest number is: {result}")