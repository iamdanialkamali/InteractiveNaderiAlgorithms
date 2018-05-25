matrix = []
lst=[]
data = list(map(int,input().split()))
for i in range(data[0]):
    for j in range(data[0]):
        lst.append(0)
    matrix.append(lst)
    lst =[]
for i in range(data[1]):
    edge = list(map(int,input().split()))
    if(matrix[edge[0]-1][edge[1]-1]==0 or matrix[edge[0]-1][edge[1]-1]>edge[2] ):
        matrix[edge[0]-1][edge[1]-1]=edge[2]
#print(matrix)
lst.append([0,0])
for j in range(1,data[0]):
    lst.append([0,99999999])
#print(lst)
seen =1
m =0
seen=[0]
while len(seen)!=data[0]+1:
    for i in range(data[0]):
        if matrix[m][i]!=0:
            if(lst[i][1]>matrix[m][i]+lst[m][1]):
                lst[i][1] = matrix[m][i]+lst[m][1]
            lst[i][0] =m
    for i in matrix:
        i[m]=999999999999999
    m = matrix[m].index(min(matrix[m]))
    seen.append(m)
#print(matrix)
print(lst[-1][1])


