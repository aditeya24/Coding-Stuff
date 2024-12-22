mark = int(input("Enter mark out of 100: "))
if mark >= 90:
    grade_point = 10 
    grade = 'S'
elif mark >= 85:
    grade_point = 9.0
    grade = 'A+'
elif mark >= 80:
    grade_point = 8.5
    grade = 'A'
elif mark >= 75:
    grade_point = 8.0
    grade = 'B+'
elif mark >= 70:
    grade_point = 7.5
    grade = 'B'
elif mark >= 65:
    grade_point = 7.0
    grade = 'C+'
elif mark >= 60:
    grade_point = 6.5
    grade = 'C'
elif mark >= 55:
    grade_point = 6.0
    grade = 'D'
elif mark >= 50:
    grade_point = 5.5
    grade = 'P'
else:
    print("Error: Marks are out of Pass Marks range")
    exit()
print(f"Grade: {grade}\nGrade Point: {grade_point}")
