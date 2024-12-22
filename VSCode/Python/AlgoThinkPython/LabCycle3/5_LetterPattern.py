N = int(input("Enter N less than 27: "))
if N<=26:
    for i in range(0,N):
        for j in range(0, i+1):
            print(chr(65+j),end=" ")
        print()
