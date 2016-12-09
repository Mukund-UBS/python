friend=[]
index=0
max=0
temp=[]
while True:
    friend.append(input())
    print(friend)
    index+=1
    if(friend[index-1]=='stop'):
        break
print("The number of friends: ",end='')
print(index-1)
for j in range(0,index-1):
    if(len(friend[j])>max):
        max=j
print("The friend with the longest name: ",end='')
print(friend[max])

print("No. of characters: ",end='')
print(len(friend[max]))
