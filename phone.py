import re
dict={}
n=int(input("Number: "))
numbers=[]
for i in range(0,n):
    name=input()
    num=int(input("Number of phone numbers: "))
    for z in range(0,num):
        numbers.append(input())
    dict[name]=list(numbers)
    numbers.clear()
print(dict)
for key in dict.keys():
    if re.search("John",key):
        print(key,end=" ")
        print(dict[key])
