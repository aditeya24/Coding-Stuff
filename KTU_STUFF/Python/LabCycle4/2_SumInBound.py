def sumInBound(lw, up):
    sum = 0
    for i in range(lw, up+1):
        sum += i 
    return sum

lower_bound = int(input("Enter Lower Bound: "))
upper_bound = int(input("Enter Upper Bound: "))

print(f"Sum: {sumInBound(lower_bound, upper_bound)}")
