# WAP to print the following pattern:
'''

*****
*   *
*   *
*   *
*****

'''
# A box of Stars

def star_pattern_four():
    
    n = int(input("Please enter the Limit of the Pattern: "))
    for i in range (1, n + 1):
        if (i == 1 or i == n):
            print("*" * n)
        else:
            print("*", end = "")
            print(" " * (n - 2), end = "")
            print("*")
    
if __name__ == '__main__':
    star_pattern_four()