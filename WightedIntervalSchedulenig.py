num =int(input())
lst= []
data =[]
for i  in range(num):
    data.append(0)
for i in range(num):
    n = input().split()
    for j in range(len(n)):
        n[j]=int(n[j])
    lst.append(n)
lst.sort(key=lambda tup: tup[1])

def binarySearch(alist, item,j):
        if len(alist) == 1:
            return j
        else:
            midpoint = len(alist) // 2
            if alist[midpoint][1] == item:
                return midpoint
            else:
                if item < alist[midpoint][1]:
                    return binarySearch(alist[:midpoint], item,midpoint)
                else:
                    return binarySearch(alist[midpoint + 1:], item,midpoint)
print(lst)

def compute(lst,data):
    for i in range(len(lst)):
        temp = data[binarySearch(lst,i,len(lst))]
        data[i]=max(lst[i][2]+temp,data[i-1])
    print(data[-1])

compute(lst,data)