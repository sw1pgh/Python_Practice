# WAP in Python to create a function to remove a given word from a list and strip it at the same time

def remove_word(input_word):
    try:
        list_words = ["Apple", "Banana", "Cherry", "Avocado", "Pear", "Tomato"]
        list_words.remove(input_word)
        print(f"These updated list of fruits is :" '\n' f"{list_words}")
        
    except:
        print(f"{input_word} does NOT exist in the List")
    
if __name__ == "__main__":
    list_words = ["Apple", "Banana", "Cherry", "Avocado", "Pear", "Tomato"]
    print(f"These are the following list of fruits:" '\n' f"{list_words}")
    inp_word = input("Enter the fruit's name that you want to remove: ")
    remove_word(inp_word)