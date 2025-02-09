# Class Methods via Class Decorator

class Class_Method:
    a = 1
    
    @classmethod
    def show(ABCDEF):
        print(f"Value of a = {ABCDEF.a}")
        
c_m_obj = Class_Method()
c_m_obj.a = 100

c_m_obj.show() # Useless laglo amar