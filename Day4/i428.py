n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
d = [abs(p[i][0]-p[i+1][0]) + abs(p[i][1]-p[i+1][1]) for i in range(len(p)-1)]
print(max(d), min(d))