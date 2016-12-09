l=[]
for i in range(6):
    l.append(int(input()))
h,m=int(input()),int(input())
s=sum(l)
def time(h,m):
    if s>60:
        h1=s//60
        m1=s-(h1*60)
        if m==0:
            print(h-h1-1,' ',60-m1)
        else:
            print(h-h1-1,' ',(60-m1)+m)
time(h,m)
