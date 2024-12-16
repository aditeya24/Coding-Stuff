n = int(input("Enter n: "))

print("Input each number: ")
num = [int(input()) for i in range(n)]
min_num = min(num)
max_num = max(num)
sum_num = sum(num)
avg_num = sum_num / n 

print(f"Max: {max_num}\nMin: {min_num}\nSum: {sum_num}\nAvg: {avg_num}")
