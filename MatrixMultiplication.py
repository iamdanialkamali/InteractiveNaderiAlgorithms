import time,random
import turtle,sys

matrix=[]
def recmatris(i, j, matris):
    if(i==j):
        return 0
    else:
        lst=[]
        for k in range(i,j):
            lst.append (recmatris(i, k, matris) + recmatris(k + 1, j, matris) + matris[i - 1] * matris[j] * matris[k])
        return min(lst)
def memmatris(i, j, matris,matrix):
    if(i==j):
        return 0
    if(i!=j ):
        if(matrix[i][j]!=2**40):
            lst=[]
            for k in range(i,j):
                lst.append (memmatris(i, k, matris,matrix) + memmatris(k + 1, j, matris,matrix) + matris[i - 1] * matris[j] * matris[k])
            target = min(lst)
            matrix[i][j]=target
            return target
        else:
            return matrix[i][j]
def dynmatrix(matris):
    n = len(matris)
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
       for i in range(1, n - L + 1):
           j = i + L - 1
           m[i][j] = 2**40
           for k in range(i, j):
               q = m[i][k] + m[k + 1][j] + matris[i - 1] * matris[k] * matris[j]
               if q < m[i][j]:
                   m[i][j]=q
    return m[1][n - 1]

"""    matrix = [[ 9999999999999999 for x in range(n)] for x in range(n)]
    for i in range(0, n):
        matrix[i][i] = 0
    for i in range(1, n-1):
        for j in range(0,n-i):
            m = (i+j)
            matrix[j][m] = 9999999999999999
            for k in range(j, m):
                q = matrix[j][k] + matrix[k + 1][m] + matris[j - 1] * matris[k] * matris[m]
                if q < matrix[j][m]:
                    matrix[j][m] = q
    return matrix[1][n - 2  ]"""

wn = turtle.Screen()
wn.bgcolor("white")
alex1= turtle.Turtle()
alex1.color('blue')
alex2=turtle.Turtle()
alex2.color('yellow')
alex3=turtle.Turtle()
alex3.color('red')
for j in range(5,19):
    print(j)
    matris=[]
    for i in range(j):
        matris.append(random.randint(1, 1000))
    matrix = [[2**40 for x in
               range(j)] for x in range(j)]
    for i in range(1, j):
        matrix[i][i] = 0
    start = time.time()
    print("recursive answer is :" + str(recmatris(1, len(matris) - 1, matris)))
    s2 = time.time()
    print("time is" + str(s2 - start))
    print("memorization answer is :", str(memmatris(1, len(matris) - 1, matris, matrix)))
    s3 = time.time()
    print("time is" + str(s3 - s2))
    print("dynamic answer is :", str(dynmatrix(matris)))
    s4 = time.time()
    print("time is" + str(s4 - s3))

    alex1.goto(5*j,5*(s2 - start))
    alex2.goto(5*j,5*(s3 - s2))
    alex3.goto(5*j,5*(s4 - s3))

wn.exitonclick()