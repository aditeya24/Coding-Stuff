#Program 6: Temperature conversion
inTempChoice = input("1. Celsius\n2. Fahrenheit\nEnter your input unit 1 or 2: ") #Select unit of input temp
if inTempChoice in ['1','2']: #Check if valid input choice
    outTempChoice = input("Enter your output unit 1 or 2: ") #Select unit of output temp
    if outTempChoice in ['1','2']: #Check if valid output choice
        inTemp = input("Enter the temperature: ") #Input temp
        match inTempChoice: #Select correct conversion using match case
            case '1':
                match outTempChoice:
                    case '1':
                        print(inTemp)
                    case '2':
                        outTemp = ((float(inTemp) * (9/5) ) + 32) #Conversion of temp from Celsius to Fahrenheit
                        print(outTemp)
            case '2':
                match outTempChoice:
                    case '1':
                        outTemp = ((float(inTemp) - 32) * (5/9) ) #Conversion of temp from Fahrenheit to Celsius
                        print(outTemp)
                    case '2':
                        print(inTemp)
    else:
        print("Error: Invalid output unit choice") 
else:
    print("Error: Invalid input unit choice")
