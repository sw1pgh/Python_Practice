# WAP in Python to build a function which will convert the temperature from Celsius to Fahrenheit

def celsius_to_fahrenheit(c):
    f = c * (9/5) + 32
    print(f"{c}°C = {f}°F")
    
if __name__ == "__main__":
    celsius_temp = float(input("Please enter the temperature in celsius: "))
    celsius_to_fahrenheit(celsius_temp)