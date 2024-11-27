N = input("Enter a number: ")
i = 1
largest = int(N[0])
while i<len(N):
  if int(N[i]) > largest:
    largest = int(N[i])
  i+=1
print(largest)