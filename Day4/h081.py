n, D = map(int, input().split())
a = list(map(int, input().split()))
r = 0
s = True
cost = a[0]

for i in range(1,len(a)):
    if (a[i] >= cost + D) and s:
        r += a[i] - cost
        cost = a[i]
        s = False
    elif (a[i] <= cost - D) and not(s):
        cost = a[i]
        s = True
print(r)
