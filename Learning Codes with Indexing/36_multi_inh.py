# Multiple Inheritance in Python

class Employee:
    name = "Swap"
    
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is God's Plan!")
        
class Coder:
    language = "Python"
    
    def printLanguages(self):
        print(f"Out of all the languages known, {self.language} is printed!")
        
class Programmer(Employee, Coder):
    company = "ITC Infotech" # Overwrite the company of the parent class
    
    def showLanguage(self):
        print(f"The name is {self.name} and he maybe knows 1% of {self.language} language")
        
inherited_prog_obj = Programmer()

inherited_prog_obj.show()
inherited_prog_obj.printLanguages()
inherited_prog_obj.showLanguage()