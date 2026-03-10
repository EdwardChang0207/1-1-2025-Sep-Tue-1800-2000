# l = input().split()
# R = int(l[0])
# C = int(l[1])
# H = int(l[2])

R, C, D = map(int, input().split())
K = int(input())

dino = [list(map(int, input().split())) for _ in range(K)]
dino_A = [True]*K
M = int(input())

for i in range(M):
    a, b, S, d = map(int, input().split())
    # a-S//2, b-S//2 ~ a+S//2, b+S//2
    for j in range(K):
        if dino[0] >= a-S//2 and dino[0] <= a+S//2:






