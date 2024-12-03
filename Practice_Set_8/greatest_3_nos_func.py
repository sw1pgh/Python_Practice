# WAP in Python to find the greatest of three numbers using function

def greatest_num(a, b, c):
    if(a > b and a > c):
        print(f"{a} is the greatest number")
    elif(b > a and b > c):
        print(f"{b} is the greatest number")
    elif(c > a and c > b):
        print(f"{c} is the greatest number")
        
def number_inputs():
    num_1 = float(input("Please enter the first number: "))
    num_2 = float(input("Please enter the second number: "))
    num_3 = float(input("Please enter the third number: "))
    greatest_num(num_1, num_2, num_3)
    
if __name__ == "__main__":
    number_inputs()