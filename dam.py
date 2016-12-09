import os
os.system('cls') #Code to clear the console.
n = int(input("Number of places from where water comes from: ")) #User inputs n
litres = []
millilitres = []
suml = 0
summl = 0
for i in range(0,n):
    litres.append(int(input("Amount in litres from place "+str(i+1)+" : "))) #Dynamic user input of litres.
    millilitres.append(int(input("Amount in milli litres from place "+str(i+1)+" : "))) #Dynamic user input of milli litres.
for j in range(0,n):
    suml = suml+litres[j] #Summation of litres.
    summl = summl+millilitres[j] #Summation of millilitres.
if(summl>1000):
    rem=summl//100
    summl=(rem%10)*100
    rem//=10
    suml+=rem
print("Total litres of water in the dam: ",suml)
print("Total millilitres of water in the dam: ",summl)
