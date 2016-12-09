def palin(s):
    pal=0
    sym=0
    n=len(s)//2
    t=s[:n]
    if len(s)%2!=0:
        t2=s[n+1:]
        if(t==t2):
            sym=1
        t2=t2[::-1]
        if(t==t2):
            pal=1
    else:
        t2=s[n:]
        if(t==t2):
            sym=1
        t2=t2[::-1]
        if(t==t2):
            pal=1
    return pal,sym
n=int(input())
l=[]
for i in range(n):
    l.append(input().lower().rstrip())
for x in l:
    pal,sym=palin(x)
    if pal==1 and sym==0:
        print("Palindrome")
    elif(pal==0 and sym==1):
        print("Symmetry")
    elif(pal==1 and sym==1):
        print("Both property")
    else:
        print("No property")
