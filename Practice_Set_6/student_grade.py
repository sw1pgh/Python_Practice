# Write a Propgram to calculate the grade of a student from his marks from the following schema:
'''
90 - 100 ==> O
80 - 90 ==> A
70 - 80 ==> B
60 - 70 ==> C
50 - 60 ==> D
< 50 ==> F
'''

import math

def grade_calculator():
    marks = []
    print(f"Enter marks of all the 3 subjects: ")
    for i in range (0,3):
        mark = int(input(f"Please enter the #{i+1} subject's marks: "))
        marks.append(mark)
    
    total_marks = sum(marks)
    before_rounding_average = total_marks / 3
    average = math.floor(before_rounding_average * 100) / 100
    
    if(average > 0 and average <=100):
        if (average >= 90 and average <=100):
            print(f"Average = {average} | Grade = O")
        elif (average >= 80 and average < 90):
            print(f"Average = {average} | Grade = O")
        elif (average >= 70 and average < 80):
            print(f"Average = {average} | Grade = O")
        elif (average >= 60 and average < 70):
            print(f"Average = {average} | Grade = O")
        elif (average >= 50 and average < 60):
            print(f"Average = {average} | Grade = O")
        elif (average < 50):
            print(f"Average = {average} | Grade = F")
    else:
        print(f"Invalid Marks Input! Re-Check and Input again...")
        grade_calculator()
        
if __name__ == "__main__":
    grade_calculator()