# Create an empty dictionary. Allow 4 friends to entire their fav language as value and set the key as their own name.
# Also find out the output if two keys are same i.e. same name.

class Trippy_Dictionary:
    
    def user_inputs(self):
        
        final_dictionary = {}
        
        for i in range (0,4):
            name = input("Please enter your name: ")
            language = input("Please enter your favourite language: ")
            final_dictionary.update({name:language})
            
        return final_dictionary
    
    def output(self):
        print(f"{self.user_inputs()}")
        
if __name__ == "__main__":
    Trippy_Dictionary().output()