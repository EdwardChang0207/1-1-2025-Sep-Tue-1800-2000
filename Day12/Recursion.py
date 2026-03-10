def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a%b)

# print(gcd(30,20))

def exp(x, n):
    if n == 0: return 1
    else: return exp(x, n-1) * x

print(exp(2,3))

def exp2(x, n):
    if n == 0: return 1
    elif n % 2 == 0: return exp(exp(x, n//2), 2)
    else: return exp(x, n-1) * x

print(exp2(2,3))

def comb(n, r):
    if r == 0 or n == r: return 1
    else: return comb(n-1, r-1) + comb(n-1, r)

print(comb(4, 2))