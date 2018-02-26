n = input()
m =input().split(" ")
m.sort()
final =[]
for i in range(len(m)-1):
    if(m[i]==m[i+1]):
        final.append(m[i])

set(final)
for i in final:
    print(i , end=" ")
