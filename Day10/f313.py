R, C, k, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(R)]
v = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for i in range(m):
    b = [[0]*C for j in range(R)]
    for row in range(R):
        for col in range(C):
            if a[row][col] == -1: continue
            d = a[row][col] // k
            for j in v:
                if row + j[0] < 0 or row + j[0] >= R or col + j[1] < 0 or col + j[1] >= C:
                    continue
                if a[row+j[0]][col+j[1]] == -1: continue
                b[row+j[0]][col+j[1]] += d
                b[row][col] -= d
    
    for row in range(R):
        for col in range(C):
            a[row][col] += b[row][col]

print(*a, sep='\n')