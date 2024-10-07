# Python program to take 6 students number as input and then sort and print it

def enter_student_marks():
    marks = [input(f"Enter {i + 1}st student's marks: ") for i in range(5)]
    marks.sort()
    print(f"Your students marks in sorted order are: {marks}")

if __name__ == "__main__":
    enter_student_marks()