# Write a program to input 8 numbers from the User and print only the unique numbers

class Unique_Numbers:
    
    def user_input(self):
        input_set = set()
        for i in range (0,8): #Loop to take 8 numbers as input into the Set
            number = input(f"Please enter the # {i+1} number: ")
            input_set.add(number)
        return input_set
    
    def unique_printing(self):
        print(f"The unique number(s) are: {self.user_input()}")
        
if __name__ == '__main__':
    Unique_Numbers().unique_printing()