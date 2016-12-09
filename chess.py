rr=int(input())
cr=int(input())
rq=int(input())
cq=int(input())
queen=(rq,cq)
rook=(rr,cr)
l1=[]
l2=[]
l3=[]
l4=[]
dqr=rq+cq
dql=cq-rq
for i in range(1,9): #/ diagonal for queen
    for j in range(1,9):
        if(i+j==dqr and (i!=rq and j!=cq)):
            t=(i,j)
            l1.append(t)
print(l1)
for i in range(1,9): #\ diagonal for queen
    for j in range(1,9):
        if(j-i==dql and (i!=rq and j!=cq)):
            t=(i,j)
            l2.append(t)
print(l2)
for i in range(1,9): # Cross for queen
    for j in range(1,9):
        if not (i==rq and j==cq):
            if(j==cq):
                t=(i,cq)
                l3.append(t)
            if(i==rq):
                t=(rq,j)
                l3.append(t)
print(sorted(list(set(l3))))
for i in range(1,9): # Cross for rook
    for j in range(1,9):
        if not (i==rr and j==cr):
            if(j==cr):
                t=(i,cr)
                l4.append(t)
            if(i==rr):
                t=(rr,j)
                l4.append(t)
print(sorted(list(set(l4))))
qpos=l1+l2+l3
rpos=l4
final = set.intersection(set(qpos),set(rpos))
print(sorted(final))
