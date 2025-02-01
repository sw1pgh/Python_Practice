# Modify Problem 2 of PS 10 to include a static method to greet the User with Hello

class Class:
    a = "Hello Citizen!"
    
    @staticmethod # decorator has been used to mark greet_user() as a static method
    def greet_user():
        print("Hello! Welcome to Python Programming...🥳")
    
OBJECT = Class()

OBJECT.a = 0

OBJECT.greet_user()

print(f"Value of a = {OBJECT.a}")