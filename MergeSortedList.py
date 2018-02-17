n = input().split(" ")
for i in range(len(n)):
    n[i] = int(n[i])
m = input().split(" ")
for i in range(len(m)):
    m[i] = int(m[i])
i ,j =0,0
final =[]
while(True):
        if(len(n)==0):
            for i in m:
                final.append(i)
            break
        if (len(m) == 0):
            for i in n:
                final.append(i)
            break
        if(n[0]<m[0] ):
           final.append(n[0])
           del n[0]
        elif (n[0]>m[0]  ):
           final.append(m[j])
           del m[0]
        elif(n[0]==m[0]):
            final.append(m[0])
            del m[0]
            del n[0]
str0 =""
for i in final:
    str0 = str0 + str(i)+" "
print(str0)