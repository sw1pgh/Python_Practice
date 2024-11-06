# WAP to find out whether a given number is prime or not

def prime_check():
    number = int(input("Please enter any number to check whether it is Prime or Not: "))
    
    if((number == 0) or (number == 1)):
        print(f"{number} is NOT a Prime Number")
    elif(number > 1):
        for i in range(2, number):
            if(number % i == 0):
                print(f"{number} is NOT a prime number")
                break
        else:
            print(f"{number} is a Prime Number")
        
if __name__ == "__main__":
    prime_check()