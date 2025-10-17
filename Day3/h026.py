F = input()
N = int(input())
s = input().split()

d = {'0':'5', '2':'0', '5':'2'}
r = False

for i in range(N):
    print(F, end=' ')
    #邊界條件
    if F == d[s[i]]: #哥哥贏
        print(f': Won at round {i+1}')
        r = True
        break
    elif s[i] == d[F]: #哥哥輸
        print(f': Lost at round {i+1}')
        r = True
        break
    else:
        if (i == 0) or (s[i] != s[i-1]): F = s[i]
        else: F = d[s[i]]

if not r: print(f': Drew at round {N}')