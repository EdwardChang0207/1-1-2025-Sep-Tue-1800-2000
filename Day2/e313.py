n = int(input())
s = sorted([input() for _ in range(n)])
cur = s[0]
for i in range(1, len(s)):
    if len(set(s[i])) < len(set(cur)):
        cur = s[i]

print(cur)