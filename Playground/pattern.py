# Print this pattern
'''
   *
  ***
 *****
*******
'''

length = int(input("Please enter the length as an integer: "))
stars = 1

for i in range (1, length + 1):
    print(" " * (length - i), "*" * (stars))
    stars += 2