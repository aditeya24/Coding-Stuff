def add(a,b):
    if b == 0:
        return a 
    else:
        return add(a+1, b-1)

a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))

print(f"Sum: {add(a,b)}")
