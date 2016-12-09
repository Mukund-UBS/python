import re
a=0
b=0
c=0
str=input("Enter the string: ")
str=str.lower()
for i in range(0,len(str)):
    if(str[i]=='q' or str[i]=='w' or str[i]=='e' or str[i]=='r' or str[i]=='t' or str[i]=='y' or str[i]=='u' or str[i]=='i' or str[i]=='o' or str[i]=='p'):
        a=1
    elif(str[i]=='a' or str[i]=='s' or str[i]=='d' or str[i]=='f' or str[i]=='g' or str[i]=='h' or str[i]=='j' or str[i]=='k' or str[i]=='l'):
        b=1
    elif(str[i]=='z' or str[i]=='x' or str[i]=='c' or str[i]=='v' or str[i]=='b' or str[i]=='n' or str[i]=='m'):
        c=1
if(a+b+c==1):
    print("Yes")
else:
    print("No")
