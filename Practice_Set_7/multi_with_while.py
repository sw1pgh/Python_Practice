# Prinitng the same table of an inputted number using while loop

def print_table_with_while():
    number = int(input("Please enter any number: "))
    product = 1
    a = 1
    print(f"The table of {number} upto 10 is:-")
    while(a<=10):
        product = number * a
        print(f"{number} * {a} = {product}")
        a = a + 1
    
if __name__ == "__main__":
    print_table_with_while()