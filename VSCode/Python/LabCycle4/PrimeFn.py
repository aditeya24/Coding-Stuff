from math import sqrt
def Prime(n, ch):
    if ch == 1:
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True 

    elif ch == 2:
        for i in range(2, n):
            if all(i % j != 0 for j in range(2, int(sqrt(i)) + 1)):
                print(i)

    elif ch == 3:
        count = 0
        i = 2
        while count < n:
            if all(i % j != 0 for j in range(2, int(sqrt(i)) + 1)):
                count += 1
                if count == n:
                    print(i)
                    break
            i += 1


ch = int(input("1. Check Prime\n2. Prime less than N\n3. Nth Prime number\nEnter choice (1,2,3): "))
N = int(input("Enter a number: "))

if ch == 1:
    if N > 1:
        print(Prime(N, ch))
    else:
        print("Error: Prime of num less than 1 not possible")
elif ch == 2 or ch == 3:
    if N > 0:
        Prime(N, ch)
    else:
        print("Error: N must be positive")
else:
    print("Error: Invalid Choice")
