string = input("Enter string: ")
freq = {x: string.count(x) for x in string}

mode = max(freq, key=freq.get)
print(f"Mode: {mode}")
