import random

def game():
    print("You are in the game now")
    score = random.randint(1, 100)
    
    with open("Practice_Set_9/Hi-score.txt") as f:
        hi_score = f.read()
        
        if (hi_score != ""):
            hi_score = int(hi_score)
            
        else:
            hi_score = 0
    
    print(f"Your score is: {score}")
    
    if (score > hi_score or hi_score == ""):
        with open("Practice_Set_9/Hi-score.txt", "w") as f:
            f.write(str(score))        

game()