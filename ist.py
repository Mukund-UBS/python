d,h,m=input(),int(input()),int(input())
days=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
f=1
p=0
m1=30+m
if m1>=60:
    t=m1//60
    h+=t+5
    m1=m1-(t*60)
else:
    h+=5
print(h,m1)
if h>=24:
    h=h-24
    for l in days:
        if l==d:
            if l=='Sunday':
                p=0
                break
            p=1+days.index(l)
            print(p)
            break
        if l not in days:
            f=0
if f!=0:
    print(days[p])
    print(h+5,m1)
else:
    print("invalid input")
