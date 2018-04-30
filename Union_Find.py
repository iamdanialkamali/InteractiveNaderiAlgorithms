n = int(input())
lst=[]
parent=[]
for i in range(n**2):
    parent.append(i)
for i in range(n):
    lst.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if(lst[i][j]==1):
            if(i!=n-1):
                if(lst[i+1][j]==lst[i][j]):
                    parent[n*(i+1)+j]=parent[n*i+j]
            if(j!=n-1):
                if (lst[i][j+1] == lst[i][j]):
                    parent[n * (i) + j+1] = parent[n * i + j]
            if(i!=n-1 and j!=n-1):
                if (lst[i + 1][j+1] == lst[i][j]):
                    parent[n * (i + 1) + j+1] = parent[n * i + j]
            if(i!=0):
                if (lst[i -1][j] == lst[i][j]):
                    parent[n * (i - 1) + j] = parent[n * i + j]
                if(j!=n-1):
                    if (lst[i -1][j+1] == lst[i][j]):
                        parent[n * (i -1) + j+1] = parent[n * i + j]
            if(j!=0):
                if (lst[i][j-1] == lst[i][j]):
                    parent[n * (i) + j-1] = parent[n * i + j]
                if(i!=n-1):
                    if (lst[i +1][j-1] == lst[i][j]):
                        parent[n * (i +1) + j-1] = parent[n * i + j]
            if(i!=0 and j!=0):
                if (lst[i -1][j-1] == lst[i][j]):
                    parent[n * (i -1) + j-1] = parent[n * i + j]

for i in range(n):
    for j in range(n):
        if(lst[i][j]==0):
            parent[n*(i)+j]=-1
#print(parent)
print(len(set(parent))-1)

