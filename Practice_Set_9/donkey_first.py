

def change_donkey(words):
    with open("Practice_Set_9/donkey.txt", "r") as f:
        content = f.read()
      
    for word in words:  
        content = content.replace(word, "#" * len(word))
    
    with open("Practice_Set_9/donkey.txt", "w") as f:
        f.write(content)
        
if __name__ == "__main__":
    word_list = ["Donkey", "Gadha", "BOT", "IDIOT"]
    change_donkey(word_list)