# Factorial Using Recursion

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1) # Function Calling itself
    
def user_input():
    num = int(input("Please enter any number: "))
    resultant_factorial = factorial(num)
    print(f'Factorial of {num} is = {resultant_factorial}')
    
if __name__ == "__main__":
    user_input()