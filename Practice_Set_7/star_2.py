# WAP to print the following pattern:
'''

*
**
***

'''

def star_pattern_two():
    
    n = int(input("Please enter the Limit of the Pattern: "))
    for i in range (1, n + 1):
        print("*" * (i))
    
if __name__ == '__main__':
    star_pattern_two()