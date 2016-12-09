from pprint import pprint
n=int(input("Number of varities: "))
d={}
sum=0
flag=1
for i in range(0,n):
    l=[]
    name=input("Name of Biscuit: ")
    for j in range(0,2):
        l.append(int(input("Contents: ")))
    d[name]=l
print(d)
q=int(input("Enter the no. of biscuits you'd like to buy: "))
for z in range(0,q):
    name=[]
    name.append(input("Enter the biscuit's name: "))
    if name[0] in d.keys():
        quan=int(input("Enter the quantity: "))
        if(quan<=d[name[0]][0]):
            d[name[0]][0]-=quan
            sum+=(quan*d[name[0]][1])
        else:
            flag=0
            break
    else:
        flag=0
if(flag==0):
    print("Order is invalid")
print("Total Cost is: ",end="")
print(sum)
#print(sorted(d.items(),key=lambda x:x[0]))
pprint(d)
