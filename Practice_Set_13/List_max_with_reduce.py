# WAP to find the maximum of the numbers in a list using the reduce function

from functools import reduce


LI_A = [1,3,100,820,56,10]

def maximum_number(a , b):
    if a > b:
        return a
    else:
        return b

max_num = reduce(maximum_number, LI_A)
print(f'Maximum Number in {LI_A} is = {max_num}')