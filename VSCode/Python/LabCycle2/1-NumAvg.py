n = int(input("Enter how many numbers: "))
print("Input each number: ")
i = 0
largest = float('-inf')
smallest = float('inf')
total_sum = 0
while i < n:
    num = int(input())
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total_sum += num
    i+=1
avg = total_sum/n 
print(f"Largest: {largest}\nSmallest: {smallest}\nSum: {total_sum}\nAverage: {avg}")
