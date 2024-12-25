
def is_word_present(word):
    with open("Practice_Set_9/log.txt", "r") as f:
        lines = f.readlines()
        
    line_no = 1
    
    for line in lines:
        if (word in line):
            print(f"{word} is present in Line Number {line_no}!")
            break
        line_no = line_no + 1
    
    else:
        print(f"Nei bhai!")
            
if __name__ == "__main__":
    is_word_present("Python")