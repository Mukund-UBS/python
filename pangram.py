s=input()
s=s.lower()
v=[x for x in s if(x.isalpha())]
print(v)
v=set(v)
if len(v)==26: print("Pangram")
else: print("Nope bruh")
