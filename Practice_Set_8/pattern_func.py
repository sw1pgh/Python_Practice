# WAP to print the first n lines of the following pattern:

'''
*****
****
***
**
*
'''

def pattern_print(n):
    a = n
    for i in range (0, n):
        print("*" * a)
        a -=1

def enter_limit():
    n = int(input("Please enter the number of lines that you wish to print: "))
    pattern_print(n)
    
if __name__ == "__main__":
    enter_limit()