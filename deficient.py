n=int(input())
l=[]
def defi():
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    s=sum(l)
    if s>n:
        print("Not deficient")
    else:
        print("Deficient")
defi()
