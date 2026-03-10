n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
p.insert(0, [0,0])
v = [[p[i+1][0]-p[i][0], p[i+1][1]-p[i][1]] for i in range(n)]
l, r, u = 0, 0, 0
for i in range(len(v)-1):
    t = v[i][0]*v[i+1][1] - v[i][1]*v[i+1][0]
    if t > 0: l += 1
    elif t < 0: r += 1
    else: u += 1
print(l, r, u)