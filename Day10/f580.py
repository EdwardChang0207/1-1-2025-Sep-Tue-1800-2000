'''
  3
5 1 2 6
  4
'''
def r(dice):
    head = dice[1].pop()
    dice[1].insert(0, head)
    return dice


def f(dice):
    side = [dice[1][-1], dice[0][1], dice[1][1]]
    dice[1][-1] = dice[2][1]
    for i in range(3):
        dice[i][1] = side[i]
    return dice

n, m = map(int, input().split())
dices = []
for i in range(n):
    dices.append([
    ['','3','',''],
    ['5','1','2','6'],
    ['','4','','']
    ])
for i in range(m):
    a, b = map(int, input().split())
    if b == -1:
        dices[a-1] = f(dices[a-1])
    elif b == -2:
        dices[a-1] = r(dices[a-1])
    else:
        t = dices[a-1]
        dices[a-1] = dices[b-1]
        dices[b-1] = t
    
for j in range(len(dices)):
    print(dices[j][1][1], end=' ')