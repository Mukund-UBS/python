x=float(input())/1000
y=float(input())/1000
z=float(input())/1000
t1=(x/3)*60
t2=(y/2)*60
t3=(z/6)*60
m=float(input())
t4=t1
t5=(y/6)*60
t6=(z/2)*60
tsum=(t1+t2+t3+m+t4+t5+t6)
final=[]
if tsum<60:
    final.append(6)
    final.append(" ")
    final.append(tsum)
else:
    final.append((tsum//60)+6)
    final.append(" ")
    final.append(tsum-((tsum//60)*60))
for z in final:
            print(z,end='')
