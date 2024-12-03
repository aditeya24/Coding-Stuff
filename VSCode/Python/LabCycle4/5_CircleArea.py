from math import sqrt, pi 

def Radius(c, pt):
    r = sqrt( (c[0] - pt[0]) ** 2 + (c[1] - pt[1]) ** 2)
    return r 

c = list(map(float, input("Enter cords of center (x,y): ").split(',')))
pt = list(map(float, input("Enter cords of point (x,y): ").split(',')))

area = pi * Radius(c, pt)
print(f"{area:.2f}")
