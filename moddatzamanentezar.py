num = input()
lst = input().split()
lst = list(map(int,lst))
lst.sort()
sum1 = 0
sum2 =0
for i in range(len(lst)-1) :
    sum1 += sum2+lst[i]
    sum2+= lst[i]
print(sum1)