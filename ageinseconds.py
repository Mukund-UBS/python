import os
os.system('cls')
n=int(input("Enter the age of the fly in days: "))
if(n>0 and n<40):
    seconds=n*24*60*60
    print("The age of the fly in seconds is: "+str(seconds))
else:
    print("Invalid input. Please enlighten yourself that an average fly could only live for about four weeks. :)")
