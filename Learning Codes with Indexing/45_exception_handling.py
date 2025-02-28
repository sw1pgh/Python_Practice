# Learn to Handle Exceptions in Python

def user_input_integer():
    try:
        ui = int(input("Please enter an integer number only: "))
        print(f"Thanks for entering an Integer")
    except Exception as e:
        print(e)
        print(f"I said only INTEGER!!!!")
        user_input_integer()
        
if __name__ == "__main__":
    user_input_integer()