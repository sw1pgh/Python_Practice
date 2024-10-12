# Python program to take n no of student's marks as input, sort the list and find the average marks

def sort_avg_list():
    marks=[]
    average_marks = 0.0
    
    nos = int(input("Please enter the number of students for which you want to enter marks: "))
    
    for i in range(0, nos):
        mark = float(input(f"Please enter #{i+1} student's mark(s): "))
        marks.append(mark)
    
    marks.sort()
    
    print(f"The marks of students in sorted order are: {marks}")
    
    if len(marks) == 0:
        print(f"Invalid Input!!!")
    else:
        total_sum = sum(marks)
        average_marks = total_sum/len(marks)
        print(f"The Average Marks of {nos} students is = {average_marks}")

if __name__ == "__main__":
    sort_avg_list()