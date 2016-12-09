import re
final=[]
p1=[]
deg1=int(input("Degree 1: "))
for i in range(-1,deg1):
    p1.append(int(input()))
p2=[]
deg2=int(input("Degree 2: "))
for j in range(-1,deg2):
    p2.append(int(input()))
min=deg1
if deg2<=min:
    min=(0-deg2)-2
else:
    min=(0-deg1)-2
for k in range(-1,min,-1):
    final.append(p2[k]+p1[k])
if(deg1!=deg2):
    if(len(p1)>len(p2)):
        for l in range(len(p1)-len(p2)-1,-1,-1):
            final.append(p1[l])
    else:
        for l in range(len(p2)-len(p1)-1,-1,-1):
            final.append(p2[l])
final.reverse()
print(p1)
print(p2)
print(final)
