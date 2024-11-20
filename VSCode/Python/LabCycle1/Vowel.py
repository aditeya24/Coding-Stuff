#Program 13: Check if character is a vowel
c = input("Enter a character: ")[0] #Take input of one character
char = c.lower() #Make character lowercase
if char in ['a','e','i','o','u']: #Check if character is vowel
    print(f"{c} is a vowel.")
else:
    print(f"{c} is not a vowel.")
