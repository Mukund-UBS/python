str=input("Enter the string: ")
x=int(input("Enter x: "))
temp=[None]*100
for i in range(0,len(str)):
    if(ord(str[i])+x>122):
        temp[i].append(chr((97)+(122-(ord(str[i])))))
    else:
        temp[i].append(chr(ord(str[i])+x))
