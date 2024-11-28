N = int(input("Enter N: "))
for i in range(1,N+1):
    print(' '*(N+1-int(i)), end="")
    c = 1
    for j in range(1,i+1):
        print(c,end=" ")
        c = c * (i - j) // j
    print()
