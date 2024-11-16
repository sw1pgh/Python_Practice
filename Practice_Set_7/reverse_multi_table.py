# WAP to print the table of an inputted number by the user using loop but the table should be in reverse order

class Multiplication_Table:
    
    def number_input(self):
        num = int(input("Please enter a number: "))
        return num
    
    def print_table(self):
        number = self.number_input()
        product = 1
        print(f"The Table of {number} is:")
        for i in range(1, 11):
            product = number * (11 - i)
            print(f"{number} * {11 - i} = {product}")
            
if __name__ == "__main__":
    Multiplication_Table().print_table()