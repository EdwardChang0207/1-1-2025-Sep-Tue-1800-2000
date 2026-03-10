n = int(input())
c = [list(map(int, input().split())) for i in  range(n)]
c.insert(0,[0,0])
f, s = 0, 0 
for i in range(len(c)):
    if c[i][0]**2 + c[i][1]**2 > c[f][0]**2 + c[f][1]**2:
        s = f
        f = i
    elif c[i][0]**2 + c[i][1]**2 > c[s][0]**2 + c[s][1]**2:
        s = i
print(*c[s])

#loop(search): n steps
#sort: nlogn step