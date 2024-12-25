def is_word_present(word):
    with open("Practice_Set_9/log.html", "r") as f:
        content = f.read()
        
        if (word in content):
            print(f"{word} is present in the file!")
        else:
            print(f"Nei bhai!")
            
if __name__ == "__main__":
    is_word_present("Python")
        