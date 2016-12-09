n=int(input())
students=[None]*100
temp = []
flag=0
if(n>=0):
    for i in range(0,n):
        students[i]=input()
    r=input()
    for i in students:
        if i not in temp:
            temp.append(i)
    for k in range(0,n):
        if(temp[k]!=None):
            print(temp[k])
            if(temp[k]==r):
                flag=1
    if (flag==1):
        print("Found")
    else:
        print("Not Found")
