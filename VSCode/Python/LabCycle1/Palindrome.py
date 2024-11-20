#Program 12: Check if Palindrome
s = input("Enter a word: ") #Input word
string = s.lower() #Make word lowercase
string_reverse = string[::-1] #Reverse word
if string == string_reverse: #Check if word is palindrome
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
