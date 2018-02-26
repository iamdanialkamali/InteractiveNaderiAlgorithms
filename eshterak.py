chrt1= input()
chrt2=input()
n = input().split(" ")
for i in range(len(n)):
    n[i] = int(n[i])
m = input().split(" ")
for i in range(len(m)):
    m[i] = int(m[i])
i ,j =0,0
final =[]
m.sort()
n.sort()
while(True):
        if(len(n)==0):
            break
        if (len(m) == 0):
            break
        if(n[0]<m[0]):
           #final.append(n[0])
           del n[0]
        elif (n[0]>m[0]  ):
           #final.append(m[j])
           del m[0]
        elif(n[0] == m[0] and len(final)==0):
            final.append(m[0])
            del m[0]
            del n[0]
        elif(n[0]==m[0] and n[0]!=final[-1]):
                final.append(m[0])
                del m[0]
                del n[0]
        elif(n[0]==final[-1]):
                del n[0]
        elif (m[0] == final[-1]):
                del m[0]
print(len(final))