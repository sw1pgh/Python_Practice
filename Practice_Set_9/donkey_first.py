

def change_donkey(changeable_word, new_word):
    with open("Practice_Set_9/donkey.txt", "r") as f:
        content = f.read()
        
    new_Content = content.replace(changeable_word, new_word)
    
    with open("Practice_Set_9/donkey.txt", "w") as f:
        f.write(new_Content)
        
if __name__ == "__main__":
    change_donkey("Donkey", "######")