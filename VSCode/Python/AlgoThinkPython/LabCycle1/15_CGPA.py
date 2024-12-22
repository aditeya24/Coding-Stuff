mark = int(input("Enter mark out of 100: "))

grade_data = [
    (90, 'S', 10),
    (85, 'A+', 9.0),
    (80, 'A', 8.5),
    (75, 'B+', 8.0),
    (70, 'B', 7.5),
    (65, 'C+', 7.0),
    (60, 'C', 6.5),
    (55, 'D', 6.0),
    (50, 'P', 5.5)
]

for threshold, grade, grade_point in grade_data:
    if mark >= threshold:
        print(f"Grade: {grade}\nGrade Point: {grade_point}")
        break
else:
    print("Error: Marks are out of Pass Marks range")
