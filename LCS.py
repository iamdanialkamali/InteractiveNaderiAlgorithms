input()
input()
seq1=input().split()
lst1=[]
lst2=[]
for i in seq1:
    lst1.append(i)

seq2=input().split()
for i in seq2:
    lst2.append(i)
seq1l=len(seq1)
seq2l=len(seq2)
matrix=[]
kmn=[]
def  LCS(seq1,seq2,i,j,kmn):
    num=0
    if(i==0 or j==0):
        return 0
    else:
        if(seq1[i]==seq2[j]):
            kmn.append(seq1[i])
            num = LCS(seq1, seq2, i - 1, j - 1, kmn) + 1
            return num
        else:
            num =(max(LCS(seq1,seq2,i,j-1,kmn),LCS(seq1,seq2,i-1,j,kmn)))
            return num
num1=LCS(lst1,lst2,seq1l-1,seq2l-1,kmn)+1
print(num1)
print(kmn[:num1].reverse())
