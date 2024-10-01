string_num_1 = input("Please enter the first number: ")
int_a = int(string_num_1)
string_num_2 = input("Please enter the second number: ")
int_b = int(string_num_2)

'''These type casting can also be done directly with the input function
int_a = int(input("Please enter a digit: "))
'''

summation = int_a + int_b

# Since by default the input() function takes string as input we need type casting for the summation to take place
# 

print(f"{int_a} + {int_b} = {summation}")