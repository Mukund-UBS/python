import os
os.system('cls')
n = int(input("Enter a number to compute the digit factor: ")) #User inputs n.
num = n
while(num>0):
    digit=num%10
    if(n%digit==0):
        if(num//10==0): #Condtional statement to avoid the comma while printing the last factor.
            print(str(digit))
            break
        else:
            print(str(digit),end=", ")
    num=num//10
