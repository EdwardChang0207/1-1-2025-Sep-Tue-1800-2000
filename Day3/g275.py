n = int(input())
for i in range(n):

    #init
    r = ''
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    #A
    for s in [s1, s2]:
        if (s[1] == s[3]) or (s[1] != s[5]): 
            r += 'A'
            break
    #B
    if (s1[-1] != 1) or (s2[-1] != 0):
        r += 'B'
    #C
    for j in range(1, 7, 2):
        if s1[j] == s2[j]:
            r += 'C'
            break
    
    #result
    if r: print(r)
    else: print('None')