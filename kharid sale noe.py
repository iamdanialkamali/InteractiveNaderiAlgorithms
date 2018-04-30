n = int(input())
tedad = int(input())
lst = input().split( )
for i in range(len(lst)-1):
    lst[i]= int(lst[i])
lst.sort()
num =0
i =0
j =len(lst)-1
while(i<j):
    if(lst[i]+lst[j]==n):
        num+=1
        i+=1
    elif(lst[i]+lst[j]<n):
        i+=1
    else:
        j-=1
print(num)