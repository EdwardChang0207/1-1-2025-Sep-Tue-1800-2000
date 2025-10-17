n = int(input())
h = list(map(int, input().split()))
r = 0
for i in range(len(h)):
    if h[i] == 0:
        if i == 0: #head
            r += h[i+1]
        elif i == n-1: #rear
            r += h[i-1]
        else:
            r += min(h[i-1], h[i+1])
print(r)