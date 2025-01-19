# Learning Class and Object in Python

class Employee: # Class
    name = "Swap"
    hobby = "Watching Football"
    title = "Ghosh"
    
    # Here [name, hobby, title] are the attributes of the class Employee --> Class attribute
    
obj_emp = Employee() # Instantiation of the Class -> Object
obj_emp.laptop = "M2 MBA" # Here laptop is the object attribute

print(f"Name = {obj_emp.name}\nLaptop = {obj_emp.laptop}")

# print(f"{Employee().name}")