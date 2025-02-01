# WAP in Python to create a class attribute a | Create an object from it and set 'a' directly using object.a = 0.
# Does this change the class attribute? : Answer -> YES, it does.

class Class:
    a = "Hello Citizen!"
    
OBJECT = Class()
OBJECT.a = 0

print(f"Value of a = {OBJECT.a}")