def recurFreq(arr, val):
    if len(arr) == 0:
        return 0
    return int(arr[0] == val) + recurFreq(arr[1:], val) 

n = int(input("Enter n: "))
arr = []
print("Input values: ")
for i in range(n):
    arr.append(input())
val = input("Enter value to check: ")
print(recurFreq(arr, val))
