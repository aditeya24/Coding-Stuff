from math import factorial as fct 

num = input("Enter a number: ")
sum = 0
for i in range(0, len(num)):
    sum += fct(int(num[i]))
if int(num) == sum:
    print(f"{num} is a Krishnamurti Number.")
else:
    print(f"{num} is not a Krishnamurti Number.")
