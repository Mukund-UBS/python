n=int(input())
final=[]
t=[]
ans=[]
c=1
for i in range(n,-1,-1):
    l=[]
    for j in range(i,n):
        s=input()
        l.append(s)
    final.append(l)
del final[0]
print(final)
for y in final:
    print(''.join(y),end='\n')

for i in final[2]:
    for j in final[1]:
        for k in final[0]:
            ans.append((i,j,k))
            print(ans)

print(ans)
