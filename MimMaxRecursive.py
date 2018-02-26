import math
def minmax(lst,i,j):
    if(i==j):
        return (lst[i],lst[i])
    else:
        if (j == i + 1):
            if (lst[i] > lst[j]):
                return (lst[j], lst[i])
            else:
                return (lst[i], lst[j])
        else:
            m=math.ceil((i+j)/2)
            Minl,Maxl=minmax(lst,i,m)
            MinR,MaxR=minmax(lst,m+1,j)
            return (min(Minl,MinR),max(MaxR,Maxl))
chert = int(input())
n = input().split()
n =list(map(int,n))
#mylst=[1,5,2,4,85,2,4,5,4]
a= minmax(n,0,len(n)-1)
print(a[0])
print(a[1])