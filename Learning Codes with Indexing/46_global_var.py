# Learning the scope and the usage of global variable

a = 90
b = 100

def func_1():
    global b
    a = 6 # Scope is limited to this function only
    b = 100 # Since scope is global, changing it's value here will change the value globally
    print(f'Func value of a = {a}')
    print(f'Func value of b = {b}\n')

func_1()
print(f'Outside value of a = {a}')
print(f'Outside value of b = {b}')
