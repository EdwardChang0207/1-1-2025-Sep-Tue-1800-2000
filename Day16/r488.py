R, C, D = map(int, input().split())
e = [[D]*C for i in range(R)]
K = int(input())
dino_P = [list(map(int, input().split())) for i in range(K)]
dino_A = [True] * K
M = int(input())

for i in range(M):
    r, c, s, d = map(int, input().split())

    a = False
    for j in range(K):
        dr, dc = dino_P[j]
        if dr >= r-s//2 and dr <= r+s//2 and dc >= c-s//2 and dc <= c+s//2:
            if dino_A[j]: 
                dino_A[j] = False
                a = True
    
    if not a:
        for j in range(r-s//2, r+s//2+1):
            for k in range(c-s//2, c+s//2+1):
                if j < 0 or j >= R or k < 0 or k >= C:
                    continue
                e[j][k] -= d

maximum, minimum = e[0][0], e[0][0]
for i in range(R):
    for j in range(C):
        if e[i][j] > maximum: maximum = e[i][j]
        if e[i][j] < minimum: minimum = e[i][j]

print(maximum, minimum, dino_A.count(True))