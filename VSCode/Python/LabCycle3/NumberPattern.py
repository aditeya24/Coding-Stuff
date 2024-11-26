N = input("Enter N: ")
i = int(N)
while i>0:
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
    i-=1
