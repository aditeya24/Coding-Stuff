#Program 4: Check largest of three numbers
a, b, c = map(int, input("Enter three numbers seperated by spaces: ").split()) #Input 3 numbers for comparision

if a > b and a > c: #Check if a is largest
    print(a)
elif b > a and b > c: #Check if b is largest
    print(b)
elif c > a and c > b: #Check if c is largest
    print(c)
else: #Output if there is no one largest number
    print("Unable to find largest number.")
