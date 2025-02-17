# Create a class 'Employee' and addSalary and add increment properties to it!

class Employee:
    
    def __init__(self):
        
        print(f"Welcome to HR Portal")
                
        self.name = input("Enter Employee Name: ")
        self.y_o_e = input("Enter Years of Experience: ")
        self.current_salary = int(input(f"Enter {self.name}'s current salary PA: "))
        
    def increment(self):
        self.appraisal_year = int(input(f"Enter {self.name}'s Year of Appraisal: "))
        self.increment_percentage = float(input("Enter Appraisal `%' in decimal value: "))
        
        self.final_appraised_salary = (self.current_salary * (100 + self.increment_percentage)) / 100
        
    def final_salary(self):
        print(f"{self.name}'s final salary after appraisal is: {self.final_appraised_salary} PA")
        
emp = Employee()
emp.increment()
emp.final_salary()