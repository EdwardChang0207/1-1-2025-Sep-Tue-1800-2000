N, M = map(int, input().split())
p = [max(map(int, input().split())) for _ in range(N)]
s = sum(p)
print(s)
p = [i for i in p if s % i == 0]
if not p: print(-1)
else: print(*p)