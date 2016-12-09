row=int(input())
column=int(input())
matrix = []
final =[]
null=0
for j in range(0,column):
    for i in range(0,row):
        matrix.append(input())
    final.append(matrix[:])
    matrix=[]
print(final)
for k in range(0,column):
    for l in range(0,row):
        if(int(final[k][l])==0):
            null+=1
if(null>=(row*column)/2):
    print("Tis Sparse")
else:
    print("Ain't sparse")
