#Program 5: Check whether given number is divisible by 3 and 7
num = int(input("Enter a number: "))
if num % 3 == 0:
    if num % 7 == 0:
        print("Number is divisible by both 3 and 7.")
    else:
        print("Number is divisible by 3 but not divisible by 7.")
elif num % 7 == 0:
    print("Number is divisible by 7 but not divisible by 3.")
else:
    print("Number is divisible by neither 3 nor 7.")
