# WAP to print the following pattern:
'''
  *
 ***
*****
'''

def star_pattern_one():
    
    n = int(input("Please enter the Limit of the Pattern: "))
    for i in range (1, n + 1):
        print(" " * (n - i), end = "")
        print("*" * (2 * i - 1), end = "")
        print("")
    
if __name__ == '__main__':
    star_pattern_one()