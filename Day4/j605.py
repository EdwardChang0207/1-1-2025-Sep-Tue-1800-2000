n = int(input())
r = [list(map(int,input().split())) for _ in range(n)]
highest = r[0][1]
highest_t = r[0][0]
wa = 0
for ti, si in r:
    if si >= highest:
        if (ti < highest_t) or (si > highest): highest_t = ti
        highest = si
    if si == -1: wa += 1
total = highest - n - wa*2
if total < 0: total = 0
print(total, highest_t) 