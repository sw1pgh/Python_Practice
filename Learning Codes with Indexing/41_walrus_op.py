# Learning the Use of the Walrus Operator

def learn_walrus():
    if (n := len([1,2,3,4,5])) > 3:
        print(f"{n} elements, Expected 3")
        
if __name__ == "__main__":
    learn_walrus()
    
# In this example, `n` is assigned the value of len([1,2,3,4,5]) and then used in comparison within the if statement