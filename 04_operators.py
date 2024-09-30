# Arithmetic Operators and Assignment Operators

'''Example 1'''
int_1 = 10
'''Here int_1 is the OPERAND and 10 is the value whereas "=" is the Assignment Operator'''
int_2 = 11
summation_value = int_1 + int_2
'''Here "+" is the Arithmetic Operator used for adding two integers'''
print(f"{int_1} + {int_2} = {summation_value}")


'''Example 2'''
int_a = 10 - 2
'''Here int_a is assigned the value of 8 directly through operations'''
int_b = 4
int_b += 10
'''Here int_b was initialized as 4 however then the command tells to increment the value of int_b by 10 and then assign the value to it'''
print(f"int_a = {int_a} \nint_b = {int_b}")


# Comparison Operators -> Return Type is always BOOLEAN

'''Example 1'''
int_c = 10
int_d = 11
print(int_c > int_d)
'''Will return False as 10 < 11 but the condition to check is if(int_c > int_d)'''