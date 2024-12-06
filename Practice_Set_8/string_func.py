# WAP in Python to create a function to remove a given word from a list and strip it at the same time

class Fruits:
    list_words = ["Apple", "Banana", "Cherry", "Avocado", "Pear", "Tomato"]
    
    def remove_word(self, input_word):
        try:
            Fruits().list_words.remove(input_word)
            print(f"These updated list of fruits is :" '\n' f"{Fruits().list_words}")
            
        except:
            print(f"{input_word} does NOT exist in the List")
    
if __name__ == "__main__":
    print(f"These are the following list of fruits:" '\n' f"{Fruits().list_words}")
    inp_word = input("Enter the fruit's name that you want to remove: ")
    Fruits().remove_word(inp_word)