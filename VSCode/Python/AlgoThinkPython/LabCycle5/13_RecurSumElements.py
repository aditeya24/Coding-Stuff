def recurSum(num):
    if len(num) == 1:
        return int(num[0])
    return int(num[0]) + recurSum(num[1:])
    

n = int(input("Enter n: "))
num = []
print("Input num: ")
for i in range(n):
    num.append(input())

print(recurSum(num))
