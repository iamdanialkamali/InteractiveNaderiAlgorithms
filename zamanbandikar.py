input()
n = input().split()
m =0
for i in range(len(n)) :
    if(m==0):
        n[i] = n[i][1:len(n[i])-1]

        m+=1
    else:
        n[i] = n[i][:len(n[i]) - 1]
        m-=1
n = list(map(int,n))
m = []
for i in range(0,len(n),2) :
    m.append([n[i],n[i+1]])
time =0
cnt =0
m.sort(key=lambda tup: tup[1])
for i in m:
    if(i[0]>=time):
        cnt+=1
        time=i[1]
print(cnt)