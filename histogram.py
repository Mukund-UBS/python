from pprint import pprint
s=input()
l2=[]
s.lower()
s=list(s)
for z in s:
    if s.isdigit():
    print("Invalid input")
    break
d={}
v={}
print(s)
for i in s:
    d[i]=s.count(i)
pprint(d)
for key, value in sorted(d.items()):
    v.setdefault(value, []).append(key)
print(v)
