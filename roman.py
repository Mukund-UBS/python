roman=input('Enter any roman numeral letter: ')
if(roman[0]=='I'):
    print("1")
elif(roman[0]=='V'):
    print("5")
elif(roman[0]=='X'):
    print("10")
elif(roman[0]=='L'):
    print("50")
elif(roman[0]=='C'):
    print("100")
elif(roman[0]=='D'):
    print("500")
elif(roman[0]=='M'):
    print("1000")
else:
    print(roman[0]+" is not a valid Roman Numeral!")
    exit()
