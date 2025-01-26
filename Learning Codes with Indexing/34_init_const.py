class Employee:
    
    def __init__(self, name):
        self.name = name
        print(f"Hello {name}")
        
    def get_Job(self):
        print(f"{self.name} works as an Automation Engineer")
        
swap = Employee("swap")
swap.get_Job()