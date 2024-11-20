#Program 14: Check if character is an alphabet or a digit
c = input("Enter a character: ")[0] #Take input of one character

if c.isdigit() is True: #Check if digit
    print(f"{c} is a digit.")
elif c.isalpha() is True: #Check if alphabet
    print(f"{c} is an alphabet.")
else: #Case where character is neither
    print(f"{c} is neither an alphabet nor a digit.")
