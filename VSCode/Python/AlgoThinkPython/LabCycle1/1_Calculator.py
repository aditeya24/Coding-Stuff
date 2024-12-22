#Program 1: Simple Calculator with 5 functions
a, b = map(float, input("Enter two numbers seperated with space: ").split()) #Input for the two numbers

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Remainder") #Print options for operations
choice = input("Enter a choice between 1-5: ") #Input choice for operation

if choice in ['1','2','3','4','5']: #Check if choice is valid
    match choice: #Match the choie with the operation
        case '1':
            print(a+b)
        case '2':
            print(a-b)
        case '3':
            print(a*b)
        case '4':
            if b != 0.0: #Checking for zero since division by zero is not defined
                print(a/b)
            else:
                print("Error: Division by zero")
        case '5':
            if b != 0.0:
                print(a%b)
            else:
                print("Error: Division by zero")
else:
    print("Error: Invalid choice")
