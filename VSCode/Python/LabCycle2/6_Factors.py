from math import sqrt
n = int(input("Enter a number: "))
factors = set()
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        factors.add(i)
        factors.add(n // i)
print(sorted(factors))
