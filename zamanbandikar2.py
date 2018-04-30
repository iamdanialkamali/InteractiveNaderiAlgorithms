input()
n = input().split()
m =0
for i in range(len(n)) :
    if(m==0):
        n[i] = n[i][1:len(n[i])-1]
        n[i]+="s"
        m+=1
    else:
        n[i] = n[i][:len(n[i]) - 1]
        n[i]+="e"
        m-=1
n.sort()
print(n)
