n = int(input("Enter how many numbers: "))
print("Enter each number and press enter: ")
odd = 0
even = 0
num = []
for i in range(0,n):
    num.append(int(input()))
    if num[i] % 2 == 0:
        even += num[i]
    else:
        odd += num[i]
print(f"Sum of odd: {odd}\nSum of even: {even}")
