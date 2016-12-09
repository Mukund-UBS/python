n1,n2=int(input()),int(input())
def ami(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    s=sum(l)
    print(l)
    print(s)
    return s
if ami(n1)==n2:
    print("Yes")
else:
    print("No")
