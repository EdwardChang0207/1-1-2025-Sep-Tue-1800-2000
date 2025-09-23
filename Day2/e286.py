r = 0
for i in range(2):
    a = map(int, input().split())sum()
    b = sum(map(int, input().split()))
    print(f'{a}:{b}')
    if a > b: r += 1
    else: r -= 1

if r > 0: print('Win')
elif r == 0: print('Tie')
else: print('Lose')