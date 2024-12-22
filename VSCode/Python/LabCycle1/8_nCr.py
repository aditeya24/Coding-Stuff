#Program 8: Compute nCr, i.e. combination
from math import factorial  #Import factorial function from math package
n = int(input("Enter n: ")) #Input total size of set n
r = int(input("Enter r: ")) #Input size of each permutation r
if n >= 0 and r >= 0: #Check if both values are positive
    nCr = factorial(n) / (factorial(r) * factorial(n-r)) #Compute combination using factorial function
    print(nCr) #Output value
else:
    print("Error: Cannot find factorial of negative numbers")
