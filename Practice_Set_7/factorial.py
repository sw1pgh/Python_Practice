# WAP in Python to find the Factorial of a number using for loop

def find_factorial():
    num = int(input("Please enter any number: "))
    factorial = 1
    
    if(num < 0):
        print(f"Factorial Does NOT exist for Negative Numbers")
        
    elif(num == 0):
        print(f"Factorial of {num} is: 1")
        
    else:
        for i in range (1, num + 1):
            factorial = factorial * i

        print(f"The factorial of {num} is: {factorial}")

if __name__ == "__main__":
    find_factorial()