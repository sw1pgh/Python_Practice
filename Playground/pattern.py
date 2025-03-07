# Print this pattern
'''
   *
  ***
 *****
*******
'''

length = int(input("Please enter the length as an integer: "))
stars = 1

for i in range (1, length):
    print(" " * (2 * length - i), "*" * (stars))
    stars += 2