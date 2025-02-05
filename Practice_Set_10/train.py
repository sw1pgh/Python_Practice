'''
Create a class Train which has methods to book a ticket, get status(no of seat) and get fare information of train running under 
INDIAN RAILWAYS
'''

import random

class Train:
    def __init__(self):
        print(f"!!!Welcome to INDIAN RAILWAYS!!!\n")
        
    def train_status(self):
        train_no = int(input("Please enter the train number: "))
        print(f"{train_no} with n number of seats is running on time!")
        exit
        
    def book_ticket(self, date, source, dest):
        print(f"Congratulations! Your ticket has been booked. Please find the ticket details below")
        print(f"Date of Journey: {date}\nSource: {source}\nDestination: {dest}\nFare: ₹ {random.randint(150, 2000)}")
        exit
        
    def get_Fare(self, source, dest):
        print(f"Please find the Fare Details for Train Number: {random.randint(12000,18000)} below:")
        print(f"Source: {source}\nDestination: {dest}\nFare: ₹ {random.randint(150, 2000)}")
        exit

if __name__ == "__main__":
    train_obj = Train()

    while True:
        try:
            user_choice = int(input('''Please tell us your requirement:\nEnter 1 -> Train Status\nEnter 2 -> Get the Fare Details\nEnter 3 -> Book Tickets\nEnter 4 -> Exit\n'''))

            if user_choice == 1:
                train_obj.train_status()
                break
            elif user_choice == 2:
                source = input("Enter source station: ")
                dest = input("Enter destination station: ")
                train_obj.get_Fare(source, dest)
                break
            elif user_choice == 3:
                date = input("Enter date of journey (DD-MM-YYYY): ")
                source = input("Enter source station: ")
                dest = input("Enter destination station: ")
                train_obj.book_ticket(date, source, dest)
                break
            elif user_choice == 4:
                print("Thank you for using Indian Railways. Have a great journey!")
                break  # Exit the loop
            else:
                print("!!! Invalid Input !!! Please enter a valid option (1-4).")
        except ValueError:
            print("!!! Invalid Input !!! Please enter a number between 1 and 4.")