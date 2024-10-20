# A spam comment is defined as a text containing the following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a Program to detect these spams.

def spam_check():
    spam_texts = ["Make a lot of money", "buy now", "subscribe this", "click this"]
    user_comment = input("Please enter any comment based on your understanding: ")
    
    # Check if any spam keywords are in the user's comment
    for spam_comment in spam_texts:
        if spam_comment in user_comment:
            print("Spam Spotted and Blocked!")
            return  # Exit the function after finding spam
    
    print("No spam detected. Your comment is safe.")

if __name__ == "__main__":
    spam_check()