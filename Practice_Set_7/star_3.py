# WAP to print the following pattern:
'''

***
* *
***

'''

def star_pattern_three():
    
    n = int(input("Please enter the Limit of the Pattern: "))
    for i in range (1, n + 1):
        if(i % 2 == 0):
            print("*", end = "")
            print(" " * (n - 2), end = "")
            print("*")
        else:
            print("*" * n)
    
if __name__ == '__main__':
    star_pattern_three()