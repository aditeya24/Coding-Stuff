def recurMax(num):
    if len(num) == 1:
        return num[0]
    return recurMax(num[1:]) if recurMax(num[1:]) > num[0] else num[0]

n = int(input("Enter n: "))
num = []
print("Input num: ")
for i in range(n):
    num.append(int(input()))

print("Max: ",recurMax(num))
