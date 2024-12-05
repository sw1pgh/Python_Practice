# WAP to create a function that converts inches to cm

def inches_to_centi(inches_value):
    centi_value = 2.54 * inches_value
    print(f"{inches_value} inches = {centi_value} cm(s)")
    
if __name__ == "__main__":
    inches_value = float(input("Please enter the value in inches: "))
    inches_to_centi(inches_value)