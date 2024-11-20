num = input('Enter a number: ')
sum = 0
for i in num:
    if int(i) % 2 == 0:
        sum = sum + int(i)
print(sum)