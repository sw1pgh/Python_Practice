# Use comparison operator to find out whether a given variable a is greater than b or not. Take both numbers as inputs

variable_a = int(input("Please enter the first variable: "))
variable_b = int(input("Please enter the second variable: "))

if (variable_a > variable_b):
    print(f"{variable_a} > {variable_b}")
elif (variable_a == variable_b):
    print(f"{variable_a} == {variable_b}")
else:
    print(f"{variable_a} < {variable_b}")
