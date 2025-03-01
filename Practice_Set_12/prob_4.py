# WAP to display a/b where a and b are integers. If b = 0, display infinite by handling the 'ZeroDivisionError'


def division_checker():
    try:
        a = int(input("Please enter first number: "))

        b = int(input("Please enter second number: "))
        
        try:
            if b == 0:
                raise ZeroDivisionError
        except:
            print(f"Infinite")

    except:
        print(f"Not a proper Integer Number")
        division_checker()
    
    else:
        try:
            print(f"{a}/{b} = {a/b}")
        except:
            pass


if __name__ == "__main__":
    division_checker()