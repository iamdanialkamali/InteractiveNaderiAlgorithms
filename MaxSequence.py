def algo(lst,i,j):
    if(i==j):
        return (lst[i])
    else:
        m = int((i+j)/2)
        maxl = algo(lst,i,m)
        maxr = algo(lst,m+1,j)
        tmp1 = 0
        tmpsuml = -999999
        for i in range(m,i-1,-1):
            tmp1 = tmp1+lst[i]
            if(tmp1>=tmpsuml):
                tmpsuml = tmp1
        tmpr = 0
        tmpsumr = -999999
        for i in range(m+1, j):
            tmpr = tmpr + lst[i]
            if (tmpr >= tmpsumr):
                tmpsumr = tmpr
        final = tmpsuml+tmpsumr
        return (max(maxr,maxl,final))
input()
lst = input().split(" ")
lst = list(map(int, lst))
print(algo(lst,0,len(lst)-1))