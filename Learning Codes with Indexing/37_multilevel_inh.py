# Multilevel Inheritance

class Coder():
    
    def __init__(self):
        print("Constructor of Coder class")
    
    a = 1

class Employee(Coder):
    
    def __init__(self):
        print("Constructor of Employee class")
    
    b = 2

class Manager(Employee):
    
    def __init__(self):
        print("Constructor of Coder class")
        super().__init__() # Super class to print the constructors of the two previous classes as well
    
    c = 3

# Each Individual Class' object will print that respective class' constructor

man_obj = Manager()
sum = man_obj.a + man_obj.b + man_obj.c
print(f"Sum = {sum}")