n = int(input())
lst =[]
for i in range(n):
    lst.append(int(input()))
def algo(lst):
    if(len(lst)==1):
        return (lst,0)
    else:
        num = 0
        final = []
        mid = len(lst)//2
        n,numr = algo(lst[mid:])
        m,numl= algo(lst[:mid])
        while (True):
            if (len(n) == 0):
                for i in m :
                    final.append(i)
                    num+=1
                break
            if (len(m) == 0):
                for i in n :
                    final.append(i)
                break
            elif (n[0] < m[0]):
                final.append(n[0])
                num += 1
                del n[0]
            elif (n[0] >= m[0]):
                final.append(m[0])
                del m[0]
        return (final,num+numl+numr)
print(int(algo(lst)[1]))