def f(x): return 2*x - 3

def g(x,y): return 2*x + y - 7

def h(x,y,z): return 3*x - 2*y + z

l = input().split()
s = []
for i in range(len(l)-1, -1, -1):
    if i == 'f':
        x = s.pop()
        s.append(f(x))
    elif i == 'g':
        x, y = s.pop(), s.pop()
        s.append(g(x,y))
    elif i == 'h':
        x, y, z = s.pop(), s.pop(), s.pop() 
        s.append(h(x, y, z))
    else:
        s.append(int(l[i]))
print(s[0])