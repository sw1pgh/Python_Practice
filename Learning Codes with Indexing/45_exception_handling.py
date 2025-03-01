# Learn to Handle Exceptions in Python

class Exceptions:
    def user_input_integer(self):
        try:
            self.ui = int(input("Please enter an integer number only: "))
            print(f"Thanks for entering an Integer")
            
        except ValueError as v:
            print(v)
            self.user_input_integer()
            
        except Exception as e:
            print(e)
            print(f"I said only INTEGER!!!!")
            self.user_input_integer()
            
    def raising_exception(self):
        self.ui_1 = int(input("Please enter first number: "))
        self.ui_2 = int(input("Please enter second number: "))
        
        if (self.ui_2 == 0):
            raise ZeroDivisionError("Second Number Cannot be Zero. Enter Second Number Again")
            self.ui_2 = int(input("Please enter second number: "))
        else:
            print(f"Div = {self.ui_1 // self.ui_2}")
    
        
exc = Exceptions()
exc.raising_exception()