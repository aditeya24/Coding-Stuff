def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

x = float(input("Enter num: "))
n = int(input("Enter power: "))

print(power(x, n))
