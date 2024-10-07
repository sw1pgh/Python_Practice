# Python Program to take 7 fruit's name as an input from the User in a List and then print them

def enter_fruits():
    fruits = [input(f"Enter fruit #{i + 1}'s name: ") for i in range(6)]
    print(f"Fruits entered: {fruits}")

if __name__ == "__main__":
    enter_fruits()