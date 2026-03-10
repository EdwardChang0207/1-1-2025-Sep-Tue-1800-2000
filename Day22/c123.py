while True:
    n = int(input())  
    if n == 0: break  
    while True:
        l = [i for i in range(1,n+1)]
        c = list(map(int, input().split()))
        if c == [0]:break
        s = []
        r = True
        for i in range(len(c)):
            while not(s) or s[-1] != c[i]:
                if not(l): 
                    r = False
                    break
                t = l.pop(0)
                s.append(t)
            if not r: break
            s.pop()
        if r: print('Yes')
        else: print('No')