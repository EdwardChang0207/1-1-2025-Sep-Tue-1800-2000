a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())

def f(a, b, c, x):
    return a*x**2 + b*x + c

y = max([f(a1, b1, c1, i)+f(a2, b2, c2, n-i) for i in range(n+1)])
print(y)