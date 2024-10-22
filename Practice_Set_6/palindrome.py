# WAP to check if an inputted number is palindrome or not using while loop

def palindrome_check():
    num = int(input("Please enter a number: "))
    ornum = num
    sum = 0
    
    while(num != 0):
        rem = num % 10
        sum = (sum * 10) + rem
        num = num // 10
    
    if (sum == ornum):
        print(f"{ornum} is a PALINDROME!")
    else:
        print(f"{ornum} is NOT a Palindrome!")

if __name__ == "__main__":
    palindrome_check()      