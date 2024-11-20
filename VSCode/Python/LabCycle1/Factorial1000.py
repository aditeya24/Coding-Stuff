#Program 11: Find no. of digits in 1000! and no. of zeros
from math import factorial
fac1000 = str(factorial(1000)) #Compute factorial of 1000 and make it string type
print(f"There are {len(fac1000)} digits in the factorial of 1000 and {fac1000.count('0')} zeros.") #Output number of digits and number of zeros
