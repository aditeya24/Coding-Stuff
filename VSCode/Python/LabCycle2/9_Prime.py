num = int(input("Enter a number: "))
i = 1
flag = 0
while i < (num-1):
    if num % (i+1) == 0:
        flag = 1
        break
    i += 1
if flag == 1:
    print(f"{num} is not a Prime number.")
elif flag == 0:
    print(f"{num} is a Prime number.")
