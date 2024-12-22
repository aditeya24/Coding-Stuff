n = int(input("Enter n: "))

print("Input each name: ")
names = [input() for name in range(n)]

names_sorted = sorted(names)

print(names_sorted)
