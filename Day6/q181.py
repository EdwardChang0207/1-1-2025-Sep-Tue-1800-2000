a, b = map(int, input().split())
n = int(input())
t = list(map(int, input().split()))
r = 0
for i in t:
    if i % (a+b) >= a:
        r += (a+b)-(i % (a+b))
print(r)