def algo(lst):
    if(len(lst)==1):
        return (lst)
    else:
        final = []
        mid = len(lst)//2
        n = algo(lst[mid:])
        m = algo(lst[:mid])
        while (True):
            if (len(n) == 0):
                for i in m :
                    final.append(i)
                break
            if (len(m) == 0):
                for i in n :
                    final.append(i)
                break
            elif (n[0] < m[0]):
                final.append(n[0])
                del n[0]
            elif (n[0] >= m[0]):
                final.append(m[0])
                del m[0]
        return final
input()
lst = input().split(" ")
lst = list(map(int, lst))
print(algo(lst))