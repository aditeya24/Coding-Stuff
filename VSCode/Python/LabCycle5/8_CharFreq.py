string = input("Enter string: ")

freq = {x: string.count(x) for x in string}

print(freq)
