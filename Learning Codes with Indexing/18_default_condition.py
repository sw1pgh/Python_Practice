# This is just a demo code to show the flow inside conditional rendering flow in Python
# Logic if you are above or at the age of 18, then only you can get a Driving License

class Driving_License:
    def user_age_input(self):
        age = int(input("Please enter your age: "))
        return age
    
    def license_logic(self):
        age = self.user_age_input()
        
        if(age > 0 and age >= 18 and age <= 70):
            print(f"You are allowed for a Driving License 🥳!")
        
        elif(age > 0 and age < 18):
            print(f"You are strictly underage!")
            
        else:
            print(f"That is a strange age for a Driving License 🙂!")
            
if __name__ == "__main__":
    Driving_License().license_logic()