input()
input()
seq1=input().split()
lst1=[]
lst2=[]
lst = []
matrix=[]

seq2=input().split()
for i in seq2:
    lst2.append(i)
    lst.append(0)


for i in seq1:
    lst1.append(i)
    matrix.append(lst)


seq1l=len(seq1)
seq2l=len(seq2)

kmn=[]
def  LCS(seq1,seq2,i,j,kmn):
    num=0
    if(i==0 and j==0):
        if(seq1[i]==seq2[j]):
            matrix[i][j]=1
            return 1
        return 0
    elif(i==0):
        n = seq1[i]
        m = seq2[j]
        if (seq1[i] == seq2[j]):
            kmn.append(seq1[i])
            num = 1
            matrix[i][j] = num
            return num
        else:
            num = matrix[i][j-1]
            matrix[i][j] = num
            return num

    elif (j == 0):
        n = seq1[i]
        m = seq2[j]
        if (seq1[i] == seq2[j]):
            kmn.append(seq1[i])
            num = 1
            matrix[i][j] = num
            return num
        else:
            num = matrix[i-1][j]
            matrix[i][j] = num
            return num

    else:
        if(i==1 and j==3):
            print(1,3)
        if(seq1[i]==seq2[j]):
            kmn.append(seq1[i])
            num = matrix[i-1][j-1] + 1
            matrix[i][j]=num
            return num
        else:
            num =(max(matrix[i][j-1],matrix[i-1][j]))
            matrix[i][j]=num
            return num
num1=LCS(lst1,lst2,seq1l-1,seq2l-1,kmn)
print(num1)