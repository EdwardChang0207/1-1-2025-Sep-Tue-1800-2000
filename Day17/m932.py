m, n, k = map(int, input().split())
b = []
p = [m-1, 0]
for i in range(m):
    r = list(input())
    for j in range(m-i-1):
        r.insert(0, '')
    b.append(r)

s = list(map(int, input().split()))
d = [[-1, 1], [0, 1], [1, 0], [1, -1], [0, -1], [-1, 0]]
r = ''
for i in s:
    p[0] += d[i][0]
    p[1] += d[i][1]
    if not(p[0] in range(0, m)) or not(p[1] in range(0, len(b[p[0]])))  or b[p[0]][p[1]] == '':
        #還原
        p[0] -= d[i][0]
        p[1] -= d[i][1]
    r += b[p[0]][p[1]]
print(r)
#set
print(len(set(list(r))))