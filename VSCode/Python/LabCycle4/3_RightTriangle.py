def isRightTriangle(a,b,c):
    side = [a,b,c]
    side.sort()
    if side[2] ** 2 == side[0] ** 2 + side[1] ** 2:
        return True
    else:
        return False

a = float(input("Enter side 1: "))
b = float(input("Enter side 1: "))
c = float(input("Enter side 1: "))

print("Is right triangle" if isRightTriangle(a,b,c) else "Is not right triangle")
