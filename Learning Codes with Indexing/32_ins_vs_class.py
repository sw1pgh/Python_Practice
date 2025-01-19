class Employee():
    language = "Python"
    name = "Swap"
    
obj_emp = Employee()
obj_emp.language = "JavaScript"

'''
Now when obj_emp.language will be printed then JavaScript will be printed instead of Python
as Instance/Object Attributes takes preference over Class Attribute
'''

print(f"Language = {obj_emp.language}")