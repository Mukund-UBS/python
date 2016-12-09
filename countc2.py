import re
from pprint import pprint 
string=input()
string=string.lower()
l=string.split(" ")
d={}
flag=1
print(l)
reg=re.compile(r'[!?,.:;]')
rn=re.compile(r'\d')
for x in range(0,len(l)):
    if(rn.findall(l[x]) or reg.findall(l[x][:-1])):
        flag=0
        break
    elif(reg.match(l[x][-1])):
       l[x]=l[x][:-1]
       d[l[x]]=l.count(l[x])
    else:
       d[l[x]]=l.count(l[x])
if flag==0:
    print("Invalid input")
else:
    pprint(d)
