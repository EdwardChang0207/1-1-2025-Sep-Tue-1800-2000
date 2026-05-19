while True:

    n = int(input())
    if n == 0:
        break
    
    while True:
        line = input().split()
        if line[0] == '0':
            print()
            break
        
        l = [int(x) for x in line]
        
        s = []
        f = 1
        b = True
        
        for i in l:
            while (not(s) or (s[-1] != i)) and (f <= n):
                s.append(f)
                f += 1
            
            if s and s[-1] == i:
                s.pop()
            else:
                b = False
                break
        
        if b:
            print("Yes")
        else:
            print("No")