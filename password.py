import re
str=input("Enter the damn password")
flag=0;
if (len(str)>=8 and str[0].isalpha()):
    flag=1
    for i in range(0,len(str)):
        if(str[i].isdigit()):
            flag+=1
            break
    for j in range(0,len(str)):
        if(str[j]>chr(31) and str[j]<chr(48)):
            flag+=1
            break
if(flag==3):
    print("Valid")
    print(flag)
else:
    print("Invalid")
    print(flag)
