from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

def PrimeLessThanN(n):
    primes =[i for i in range(2,n) if isPrime(i)]
    return primes

def NthPrime(n):
    count = 0
    i = 2
    while count < n:
        if isPrime(i):
            count += 1
            if count == n:
                return i
        i += 1

N = int(input("Enter a number: "))

if N > 1:
    print(f"{N} is prime" if isPrime(N) else f"{N} is not prime")
    print(f"Prime less than {N}: {PrimeLessThanN(N)}")
    print(f"{N}th Prime number: {NthPrime(N)}")
else:
    print("Error: Prime of num less than 1 not possible")
    
