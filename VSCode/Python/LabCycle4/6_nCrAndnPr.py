def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

n_fct = factorial(n)
r_fct = factorial(r)
nr_fct = factorial(n-r)

nCr = n_fct / ( r_fct * nr_fct)
nPr = n_fct / nr_fct

print(f"nCr: {nCr}\nnPr: {nPr}")
