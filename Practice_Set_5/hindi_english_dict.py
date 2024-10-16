class Hindi_English:

    def hindi_english(self):
        language_dictionary = {
            "kursi": 'chair',
            'kitaab':'book',
            'paani':'water'
        }
        return language_dictionary

    def user_lookup(self):
        print(f"\nAvailable words are:\n'- kursi'\n'- kitaab'\n'- paani'\n")
        lookup_word = input("Please enter the word whose English translation you want: ")
        
        
        translated_word = self.hindi_english().get(lookup_word)
        
        if translated_word:
            print(f"The translation is: {translated_word}")
        else:
            print(f"You have chosen a wrong word\nTry Again!!!")
            self.user_lookup()
        
if __name__ == "__main__":
    Hindi_English().user_lookup()