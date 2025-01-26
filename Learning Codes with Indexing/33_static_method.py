class static_method_try:
    
    @staticmethod # decorator has been used to mark greet_user() as a static method
    def greet_user():
        print("Hello! Welcome to Python Programming...🥳")
        
st_mt = static_method_try()
st_mt.greet_user()