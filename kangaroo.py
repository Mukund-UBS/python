s=input()
s2=input()
sec=[]
index=[]
c=0
l=[x for x in s2]
for i in range(0,len(s)):
    if s[i]==l[0]:
        sec=s[i:]
        c=i
for z in s2:
    if z in sec:
        index.append(l.index(z)+c)
print(index)
print(sec)
def kangaroo():
    if(sorted(index)==index and index!=[] and (len(index)==len(s2))):
        print("True")
    else:
        print("False")
kangaroo()
