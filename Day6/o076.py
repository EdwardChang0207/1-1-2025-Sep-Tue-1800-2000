n = int(input())
h = list(map(int, input().split()))
max_p, p = 0, 1
for i in range(1, len(h)):
    if h[i] < h[i-1]: 
        p += 1
        if p > max_p: 
            max_p = p
    else:
        p = 1        
print(max_p)