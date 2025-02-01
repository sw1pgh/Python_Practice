# WAP in Python to create a class "Calculator" capable of finding square, cube and square root of a number

import math

class Calculator:
    
    def __init__(self):
        self.input_number = int(input("Please enter a Number: "))
    
    def square(self):        
        square_value = float(self.input_number ** 2)
        print(f"The square of {self.input_number} is = {square_value}")
        
    def cube(self):
        cube_value = float(self.input_number ** 3)
        print(f"The cube of {self.input_number} is = {cube_value}")
        
    def square_root(self):
        square_root_value = math.sqrt(self.input_number)
        print(f"The Square Root of {self.input_number} is = {square_root_value}")
        
if __name__ == "__main__":
    obj_calc = Calculator()
    obj_calc.square()
    obj_calc.cube()
    obj_calc.square_root()