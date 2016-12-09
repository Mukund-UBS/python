from pprint import pprint
import re
string=""
flag=1
d=[]
special=[]
spec=[]
final=[]
string=input()
string=string.strip()
string=string.lower()
l=string.split(" ")
print(l)
for i in range(0,len(l)):
    d=[]
    rex=re.compile(r'\d')
    if rex.findall(l[i]):
        flag=0
        break
    reg=re.compile(r'\W')
    if reg.findall(l[i]):
        matches=reg.findall(l[i])
        if not re.findall(l[i][-1],r'[!?.:;,]') or len(matches)>1:
            flag=0
            break
        else:
            spec.append(l[i][:-1])
            d=(spec[i],)
            d+=(spec.count(spec[i]),)
            final.append(d)
    else:
        spec.append(l[i])
        d=(spec[i],)
        d+=(spec.count(l[i]),)
        final.append(d)
if flag==0:
    print("Invalid Input")
else:
    print(final)
    print(final)
    z=set(final)
    s={x:y for (x,y) in z}
    pprint(s)
