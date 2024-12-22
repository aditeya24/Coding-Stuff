s = input("Enter a string: ")
splitstring = s.split()
words = len(splitstring)
letter = digit = words = upper = lower = 0

for i in range(0, len(s)):
    if s[i].isupper():
        upper += 1
    elif s[i].islower():
        lower += 1
    elif s[i].isdigit():
        digit += 1
letter = upper + lower
print(f"Letter: {letter}\nDigit: {digit}\nWords: {words}\nUppercase: {upper}\nLowercase: {lower}")
