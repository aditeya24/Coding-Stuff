name = input('Enter name: ')
n = int(input('Enter number of subjects: '))
maxmarks = int(input('Enter maximum marks for each subject: '))
marks = []

for i in range(n):
    iterativemarks = int(input(f'Enter marks of Subject {i+1}: '))
    marks.append(iterativemarks)

total = sum(marks)
average = total / len(marks)
percentage = (average / maxmarks) * 100

print(f'Total marks: {total}\nAverage marks: {average}\nPercentage: {percentage}')