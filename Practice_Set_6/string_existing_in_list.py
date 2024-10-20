# WAP in Python to check whether an inputted name is present in a List or not?

def check_name():
    name_list = ["Swap", "Ram", "swap", "Swapnaneel", "Swap.GG"]
    name_input = input("Please Enter your Name: ")
    
    if name_input in name_list:
        print(f"We have your name in the list!")
    else:
        print(f"You are an alien to us!!!")
        
if __name__ == "__main__":
    check_name()