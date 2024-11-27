import math
x = float(input("Enter x in degrees: "))
n = int(input("Enter n: "))
x *= math.pi/180
sum = 0
for i in range(n+1):
    term = (((-1)**i)*(((x)**(2*i))/math.factorial(2*i)))
    sum += term
    sum = round(sum,4)
print("Sum: ", sum)