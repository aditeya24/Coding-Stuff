n = int(input("Enter n: "))

prev1 = 1 
prev2 = 0

print(prev2, end=" ")

if n == 1:
    print()
    exit()

print(prev1, end=" ")

curr = 0

while curr < n:
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr
    print(curr, end=" ") 
print()
