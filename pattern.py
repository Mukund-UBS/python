import os
os.system('cls') #Code to clear the console.
n = int(input("Enter the number of rows for the pattern: ")) #User inputs n.
n=n*2
for i in range(2,n+1,2): #number of rows
    for j in range (1,i+1): #elements in a row.
        print("*",end =" ")
    print("\n") #line break after each row.
