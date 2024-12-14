import random
from enum import Enum

class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

class RockPaperScissorsGame:
    
    def get_random_choice_from_computer(self):
        # Randomly select one of the valid choices
        return random.choice(list(Choice))
    
    def print_statements(self):
        # Print the game rules
        print('''
            :RULES:
                        
            -> Rock wins against Scissors;
            -> Paper wins against Rock; and
            -> Scissors wins against Paper.
        ''')
        
    def get_user_input(self):
        # Mapping user input to Choice enum
        user_choice_map = {
            1: Choice.ROCK,
            2: Choice.PAPER,
            3: Choice.SCISSORS
        }
        
        # Prompt user for input and validate
        print("Enter your choice:")
        print("1 - rock")
        print("2 - paper")
        print("3 - scissors")
        
        while True:
            try:
                user_input = int(input("Choose 1, 2, or 3: "))
                if user_input in user_choice_map:
                    return user_choice_map[user_input]
                else:
                    print("Invalid choice, please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input, please enter a number.")
                
    def determine_winner(self, user_choice, computer_choice):
        # Define rules for determining the winner
        outcome = {
            (Choice.ROCK, Choice.SCISSORS): "You win!",
            (Choice.PAPER, Choice.ROCK): "You win!",
            (Choice.SCISSORS, Choice.PAPER): "You win!",
            (Choice.SCISSORS, Choice.ROCK): "You lose!",
            (Choice.ROCK, Choice.PAPER): "You lose!",
            (Choice.PAPER, Choice.SCISSORS): "You lose!"
        }
        
        # Check if it's a tie
        if user_choice == computer_choice:
            print("It's a tie!")
        else:
            print(outcome.get((user_choice, computer_choice), "Invalid choice"))
        
        # Show choices
        print(f"\nComputer's Choice: {computer_choice.value}")
        print(f"Your Choice: {user_choice.value}")
        print("\n")

if __name__ == "__main__":
    rps_game = RockPaperScissorsGame()
    
    rps_game.print_statements()
    
    while True:
        # Get random computer choice and user input
        computer_choice = rps_game.get_random_choice_from_computer()
        user_choice = rps_game.get_user_input()
        
        # Determine winner
        rps_game.determine_winner(user_choice, computer_choice)
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break