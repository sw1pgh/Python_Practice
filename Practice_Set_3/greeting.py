from datetime import datetime

def name_input():
    input_name = input("Please enter your name: ")
    return input_name

def get_greeting() -> str:
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    elif 18 <= current_hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

if __name__ == "__main__":
    print(f"{get_greeting()} {name_input()}!")