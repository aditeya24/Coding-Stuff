def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

num = list(map(int, input("Input num seperated by spaces: ").split()))

num_prime = [i for i in num if isPrime(i)]
num_composite = [i for i in num if not isPrime(i)]

print(f"Prime: {num_prime}\nComposite: {num_composite}")
