# Take input as marks of 3 different subjects from the User and determine if he/she passed or failed.
# Passing Concition: Avergae >= 40 and >= 33 in each subject

def get_marks(subject):
    """Get valid marks for a subject."""
    while True:
        try:
            marks = int(input(f"Please enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_average(marks):
    """Calculate the average of a list of marks."""
    return sum(marks) / len(marks)

def determine_pass_fail(marks):
    """Determine if the student passed or failed based on marks."""
    if all(mark >= 33 for mark in marks) and calculate_average(marks) >= 40:
        return True
    return False

def main():
    subjects = ["Maths", "Computer", "English"]
    marks = [get_marks(subject) for subject in subjects]

    if determine_pass_fail(marks):
        print("Congratulations! You have passed the examination.")
    else:
        print("You have failed! Good luck for next time.")

if __name__ == "__main__":
    main()