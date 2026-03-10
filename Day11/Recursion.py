'''
等差數列


a1, d, n = 1, 2, 5
for i in range(n):
    print(a1+i*d)

def a(a1, d, n): #收斂
    if n == 0: return #邊界條件 終止條件
    print(a1)
    return a(a1+d, d, n-1)#繼續下去

a(a1, d, n)

def a(a1, d, n):
    if n == 1:
        print(a1)
        return
    else:
        print(a1 + (n-1)*d)
        return a(a1, d, n)
    
def s(a1, d, n):
    if n == 1: return a1
    return s(a1, d, n-1) + a1 + (n-1)*d

print(s(a1, d, n))


def b(b1, r, n):
    if n == 1: return b1
    return b(b1, r, n-1) * r

def s(b1, r, n):
    if n == 1: return b1
    return s(b1, r, n-1) + b(b1, r, n)

b1, r, n = 1, 2, 4
print(s(b1,r,n))

def f(n):
    if n == 0: return 0
    if n == 1: return 1
    return f(n-1) + f(n-2)

print(f(5))

def A(m, n):
    if m == 0: return n+1
    if n == 0 and m > 0:
        return A(m-1, 1)
    return A(m-1, A(m, n-1))

print(A(2, 3))
'''

def exp(x, n):
    if n == 0: return 1
    return exp(x, n-1) * x

def exp2(x, n):
    if n == 0: return 1
    if n % 2 == 0:
        return exp(exp(x, n//2), 2)
    return exp(x, n-1) * x

print(exp(2, 5))
print(exp2(2, 5))