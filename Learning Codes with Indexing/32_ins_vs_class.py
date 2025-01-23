class Employee():
    language = "Python"
    name = "Swap"
    
    def getInfo(self): # self is a function parameter as whenever we create any function in python, an empty paramter named 
        print(f"The language is {self.language} and the name is {self.name}")
        
    def greet(self):
        print("Good Morning!")
    
obj_emp = Employee()
obj_emp.language = "JavaScript"

'''
Now when obj_emp.language will be printed then JavaScript will be printed instead of Python
as Instance/Object Attributes takes preference over Class Attribute
'''

print(f"Language = {obj_emp.language}")
obj_emp.greet()
obj_emp.getInfo()