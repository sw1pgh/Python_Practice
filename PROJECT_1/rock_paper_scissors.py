'''
The rock is a closed fist;
paper is a flat hand with fingers and thumb extended and the palm facing downward;
and scissors is a fist with the index and middle fingers fully extended toward the opposing player.
Rock wins against Scissors;
Paper wins against Rock; and
Scissors wins against Paper.
'''

import random

class Rock_Papaer_Scissors_Game:
    
    def get_random_choice_from_computer():
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
    
    def print_statements():
        print(f''''
            The rock is a closed fist;
            paper is a flat hand with fingers and thumb extended and the palm facing downward;
            and scissors is a fist with the index and middle fingers fully extended toward the opposing player.
            Rock wins against Scissors;
            Paper wins against Rock; and
            Scissors wins against Paper.
            ''')
        print("")
        
    def get_user_input():
        print("Enter your choice:")
        print("1 - rock")
        print("2 - paper")
        print("3 - scissors")
        
        while True:
            try:
                user_input = int(input("Choose 1, 2, or 3: "))
                if user_input == 1:
                    return "rock"
                elif user_input == 2:
                    return "paper"
                elif user_input == 3:
                    return "scissors"
                else:
                    print("Invalid choice, please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input, please enter a number.")
                
    def determine_winner(user_choice, computer_choice):
        # Rules of Rock, Paper, Scissors
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
                return "You win!"
        else:
            return "You lose!"
        
    user_choice = get_user_choice()
    computer_choice = get_random_choice()