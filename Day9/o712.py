M, N, k, r, c = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(M)]
d = [[0, 1],[1, 0],[0, -1],[-1, 0]]
facing = 0
score = 0
amount = 0
while game_map[r][c] != 0:
    score += game_map[r][c]
    amount += 1
    game_map[r][c] -= 1
    if score % k == 0: facing = (facing+1)%4
    while r+d[facing][0] >= M or r+d[facing][0] < 0 or c+d[facing][1] >= N or c+d[facing][1] < 0 or game_map[r+d[facing][0]][c+d[facing][1]] == -1:
        facing = (facing+1)%4
    r += d[facing][0]
    c += d[facing][1]
print(amount)