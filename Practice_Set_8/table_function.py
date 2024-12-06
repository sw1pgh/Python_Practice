# WAP in Python to print the table of any given number with function

def table_num(num):
    product = 1
    for i in range (1, 11):
        product = num * i
        print(f"{num} * {i} = {product}")
        
if __name__ == "__main__":
    number = int(input("Please enter any number: "))
    table_num(number)