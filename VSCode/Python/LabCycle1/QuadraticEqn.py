#Program 10: Find roots of a Quadratic equation
a, b, c = list(map(int, input("Enter numbers a, b, c seperated by spaces: ").split())) #Input three constant values of Quadratic eqn
if a != 0: #Check if a is non-zero
    d = (b ** 2) - (4 * a * c) #Compute discriminant
    root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) #Compute first root
    root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) #Compute second root
    if d == 0: #Check case where there is only one root
        print(f"The root of the Quadratic equation is {root1}")
    else:
        print(f"The roots of the Quadratic equation are {root1} and {root2}")
else:
    print("Error: a cannot be 0")
