m, n = map(int, input().split())
A = [list(map(int, input().split())) for i in range(m)]
AT = []

for i in range(n):
    col = []
    for j in range(m):
        col.append(A[j][i])
    AT.append(col)

for row in AT:
    print(*row)