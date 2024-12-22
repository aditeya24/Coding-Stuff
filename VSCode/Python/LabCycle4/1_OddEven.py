def oddEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a num: "))
print("Even" if oddEven(n) else "Odd")
