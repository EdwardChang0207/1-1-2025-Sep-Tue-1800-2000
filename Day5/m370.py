x, n = map(int, input().split())
f = list(map(int, input().split()))

l, r = 0, 0
for i in f:
    if i < x: l += 1
    elif i > x: r += 1

if l > r: print(l, min(f))
else: print(r, max(f))