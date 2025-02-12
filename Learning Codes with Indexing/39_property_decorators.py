# Property Decorators
class Class_Method:
    a = 1
    
    @classmethod
    def show(ABCDEF):
        print(f"Value of a = {ABCDEF.a}")
        
    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
c_m_obj = Class_Method()
c_m_obj.a = 100

c_m_obj.name = "Swap GG"
print(f"{c_m_obj.fname}")
print(f"{c_m_obj.lname}")

c_m_obj.show() # Useless laglo amar