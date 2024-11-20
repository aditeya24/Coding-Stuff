s = input("Enter a string: ")

count = 0
for i in range(0, len(s)):
    if s[i] in "aeiou":
        count += 1
print(f"Number of vowels: {count}")
