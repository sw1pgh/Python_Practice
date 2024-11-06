# WAP to print the sum of first N natural numbers

def sum_Natural():
    limit = int(input("Please enter the limit: "))
    sum = 0
    a = 1
    while(a <= limit):
        sum = sum + a
        a = a + 1
    
    print(f"The sum is: {sum}")
    
if __name__ == "__main__":
    sum_Natural()