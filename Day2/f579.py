a, b = map(int, input().split())
n = int(input())
carts = [sorted(list(map(int, input().split()))) for _ in range(n)]
r = 0
for cart in carts:
    for i in cart:
        if i >= 0: break
        cart.remove(-i)
    if (a in cart) and (b in cart): r += 1
print(r)