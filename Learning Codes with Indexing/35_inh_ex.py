class Employee:
    company = "ITC"
    
    def show(self):
        print(f"The name of the Employee is Swap and the salary is God's Plan!")
        
class Programmer(Employee):
    company = "ITC Infotech" # Overwrite the company of the parent class
    
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")
        
a = Employee()
b = Programmer()

print(f"{a.show()}")
print(f"A = {a.company}\nB = {b.company}")