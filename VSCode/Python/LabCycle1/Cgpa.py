#Program 15: Calculate KTU Grade and Grade Point
mark = int(input("Enter the mark out of 100: ")) #Input mark
if mark >= 50 and mark < 55: #Check if mark is within range of grade
    grade_point = 5.5
    grade = 'P'
elif mark >= 55 and mark < 60:
    grade_point = 6.0
    grade = 'D' 
elif mark >= 60 and mark < 65:
    grade_point = 6.5
    grade = 'C' 
elif mark >= 65 and mark < 70:
    grade_point = 7.0
    grade = 'C+'
elif mark >= 70 and mark <  75:
    grade_point = 7.5
    grade = 'B'
elif mark >= 75 and mark < 80:
    grade_point = 8.0
    grade = 'B+'
elif mark >= 80 and mark < 85:
    grade_point = 8.5
    grade = 'A'
elif mark >= 85 and mark < 90:
    grade_point = 9.0
    grade = 'A+'
elif mark >= 90:
    grade_point = 10 
    grade = 'S'
else:
    print("Error: Marks are out of Pass Marks range") #Case where mark is not within pass range
    exit() #Stop running program
print(f"Grade: {grade}\nGrade Point: {grade_point}")
