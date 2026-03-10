m, n = map(int, input().split())
m1 = [[int(i) for i in input().split()] for r in range(m)]
m2 = [[int(i) for i in input().split()] for r in range(m)]

#1.m1 + m2 -> m3
m3 = []
for r in range(m):
    row = []
    for c in range(n):
        row.append(m1[r][c] + m2[r][c])
    m3.append(row)

for r in m3:
    print(*r)
    
#2.m1 (+)-> m2
for r in range(m):
    for c in range(n):
        m2[r][c] += m1[r][c]

for r in m2:
    print(*r)