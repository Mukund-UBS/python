str=input('')
count=0
for i in range(0,len(str)):
    for j in range(i+1,len(str)):
        if(str[i]==str[j]):
            count=count+1
if(count==0):
    print("Distinct.")
else:
    print("Not distinct.")
