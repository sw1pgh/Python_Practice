# WAP in Python to find out whether a string contains a word or not

def is_word_present():

    max_length = 1000
    input_string = input("Please enter a paragraph: ")[:max_length]
    
    user_word = input("Please enter a word to check if it's present in the paragraph or not: ")
    
    if user_word.lower() in input_string.lower():
        print(f"{user_word} is present in the Paragraph!")
    else:
        print(f"{user_word} is MISSING!!!")
        
if __name__ == "__main__":
    is_word_present()