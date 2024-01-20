size = input().split()
n = int(size[0])
m = int(size[1])

A = []
B = []

for i in range(n):
    cola = []
    colb = []
    for j in range(m):
        cola.append(0)
        colb.append(0)
    A.append(cola)
    B.append(colb)

for i in range(n):
    a = input().split()
    for j in range(m):
        A[i][j] = a[j]

for i in range(n):
    b = input().split()
    for j in range(m):
        B[i][j] = b[j]

for i in range(n):
    for j in range(m):
        print(int(A[i][j]) + int(B[i][j]), end=" ")
