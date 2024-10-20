# WAP in Python to detect whether a Username contains less than 10 characters or not?

def username_check():
    username_input = input("Please enter your Username: ")
    character_count = len(username_input)
    
    if (character_count > 0 and character_count < 10):
        print(f"Username Invalid! Contains less than 10 characters")
    elif(character_count <= 0):
        print(f"Please enter something!!!")
        username_check()
    else:
        print(f"Valid Username!")

if __name__ == "__main__":
    username_check()