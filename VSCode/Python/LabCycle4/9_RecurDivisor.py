def divisor(a,b):
    if b == 0:
        return a 
    else:
        return divisor(b, a%b)

a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))

if a >= 0 and b >= 0:
    print(f"Greatest Common Divisor: {divisor(a,b)}")
else:
    print("Error: Enter positive numbers")
