from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

n = int(input("Enter a number: "))
factors = set()
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        factors.add(i)
        factors.add(n // i)

f_prime = [i for i in sorted(factors) if isPrime(i)]
print(*f_prime)
