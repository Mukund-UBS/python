n=int(input())
id=[]
height=[]
temp=[]
order=[]
final=[]
for i in range(0,n):
    id.append(int(input("ID: ")))
    height.append(int(input("Height: ")))
temp=height[:]
temp.sort()
for j in range(0,n):
    for k in range(0,n):
        if(temp[j]==height[k]):
            order.append(k)
for k in range(0,n):
    final.append(id[order[k]])
print(final)
