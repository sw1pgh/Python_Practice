# WAP in Python to greet only the persons present in a list l who have S as their first characters

def selective_greeting():    
    l = ["Sam", "John", "Sophie", "Alice", "Steve", "Maggie"]
    
    print(f"Greetings my dear ")
    
    for name in l:
        if name.startswith('S'):
            print(f"{name}!")

if __name__ == "__main__":
    selective_greeting()