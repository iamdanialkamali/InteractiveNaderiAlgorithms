n =int(input())
var=[]
freq=[]
keys=[]
for i in range(n):
    var = input().split()
    keys.append(var[0])
    freq.append(int(var[1]))
lenght = len(freq)
tajmie=[]
def tajmie(freq,i,j):
    sum =0
    for m in range(i,j+1):
        sum+=freq[m]
    return sum
def optimaltree(freq,i,j):
    if(i>j):
        return 0
    if(i==j):
        return freq[i]
    else:
        lst=[]
        for k in range(i,j+1):
            lst.append(optimaltree(freq,i,k-1)+optimaltree(freq,k+1,j)+tajmie(freq,i,j))
        if(i==0 and j==len(freq)-1):
            print(keys[i+lst.index(min(lst))])
        return min(lst)
optimaltree(freq,0,lenght-1)