# Multilevel Inheritance

class Coder():
    a = 1

class Employee(Coder):
    b = 2

class Manager(Employee):
    c = 3

man_obj = Manager()
sum = man_obj.a + man_obj.b + man_obj.c
print(f"Sum = {sum}")