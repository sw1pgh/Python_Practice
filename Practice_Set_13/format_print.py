# WAP to input name, marks and phone number of a student and format it using the format function like below.
# "The name of the student is Harry, his marks is 72 and phone number is 9999999"

class Format_Output:
    
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.marks = int(input("Please enter your marks in Integer value: "))
        self.mob_num = int(input("Please enter your mobile number without country code: "))
        
    def output(self):
        return print("The name of the student is {}, his marks is {} and phone number is {}".format(self.name, self.marks, self.mob_num))

Format_Output().output()