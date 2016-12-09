import math
n=int(input())
d={}
l=[]
mini=[]
min=100
for i in range(0,n):
    x=int(input())
    y=int(input())
    t=(x,y)
    l.append(t)
for j in range(0,n):
    for k in range(j+1,n):
        d[l[j],l[k]]=round(math.sqrt((l[j][0]-l[k][0])**2 + (l[j][1]-l[k][1])**2),2)
for x,y in d.items():
    if y<min:
        min=y
        minim=x
mini.append(minim)        
del d[mini[0]]
for x,y in d.items():
    if y==min:
        mini.append(x)
print(mini)
print(d)
for z in range(0,len(mini)):
    print(mini[z][0])
    print(mini[z][1])
