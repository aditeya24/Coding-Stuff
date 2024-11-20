n = int(input("Enter how many numbers: "))
print("Enter each number and press enter: ")
num = []
for i in range(0, n):
  num.append(int(input()))
max = max(num)
min = min(num)
sum = sum(num)
avg = sum/n 
print(f"Largest number: {max}\nSmallest number: {min}\nSum: {sum}\nAverage: {avg}")
