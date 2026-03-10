import sys
for i in sys.stdin: #standard input
    m, n = map(int, i.split())
    A = [list(map(int, input().split())) for i in range(m)]
    AT = []
    for i in range(n):
        col = []
        for j in range(m):
            col.append(A[j][i])
        AT.append(col)
    for r in AT:
        print(*r)