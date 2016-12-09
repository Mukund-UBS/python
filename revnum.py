n=input()
def reverse(num):
    rev=num[::-1]
    return rev
rev=reverse(n)
s1=int(n)**2
s2=int(rev)**2
temp=reverse(str(s2))
if(int(temp)==s1):
    print("ADAM!")
else:
    print("NOT ADAM!")
