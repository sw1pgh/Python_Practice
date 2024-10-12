# Python program to take 6 students number as input and print it in sorted order

def enter_student_marks():
    marks = []
    for i in range(6):  # Changed to 6 to get marks for 6 students
        mark = float(input(f"Enter #{i + 1} student's marks: "))  # Convert input to float
        marks.append(mark)  # Append the mark directly to the list
    
    marks.sort()  # Sort the list of marks
    print(f"Your students' marks in sorted order are: {marks}")

if __name__ == "__main__":
    enter_student_marks()