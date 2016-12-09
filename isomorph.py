from pprint import pprint
n=int(input())
l=[]
for i in range(0,n):
    l.append(input())
def palin(a):
    index=[]
    for k in a:
        index.append(a.index(k))
    return index
    print(index)
final=[]
check=[p for p in range(1,n+1)]
for i in range(1,n):
    if palin(l[0]) == palin(l[i]):
        final.append(l[i])
print(l[0])
for z in final:
    print(z)
