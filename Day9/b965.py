def f(m:list):
    m.reverse()
    return m

def r(m:list):
    new = []
    for col in range(len(m[0])):
        r = []
        for row in range(len(m)):
            r.append(m[row][col])
        new.append(r)
    r.reverse()
    m = r
    return m

R, C, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(R)]
k = list(map(int, input().split()))

k.reverse()
for i in k:
    if i == 0:
        B = f(B)
    else:
        B = r(B)

print(len(B), len(B[0]))
for row in B:
    print(*row)
