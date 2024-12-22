f = lambda x : (x**2) + (3 * x) + 2
g = lambda x, y: (2 * x**3) + (3 * y**2) + (4 * x * y) + 2

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f"f({x}) = {f(x)}\ng({x},{y}) = {g(x,y)}")
