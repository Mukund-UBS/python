import os
os.system('cls')
n1=int(input("Enter the first number: ")) #User inputs the first number.
n2=int(input("Enter the second number: ")) #User inputs the second number.
counter=0 #Counter to check the number of primes factors common.
if n2>n1:
    max=n2
    min=n1
else:
    max=n1
    min=n2
for i in range(1,max+1):
        if(max%i==0 and min%i==0): #Comparing the common factors.
            counter=counter+1
if(counter==1): #If two numbers have one common coprime, it could only be 1.
    print("The numbers are coprime!")
else:
    print("The numbers are not comprime.")
