n, d = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
r, p = 0, 0
for i in items:
    if max(i) - min(i) >= d:
        r += 1
        p += sum(i)//3
print(r, p)