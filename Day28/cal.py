'''
input: postfix output: ans

num: push
op: pop相應數量的數字，算完再放回

+-*/
4 3 - -> 4 - 3
[4, 3]
3 ->b
4 ->a
a-b
'''

l = input().split()
s = []
for i in l:
    if i in '+-*/':#op
        b, a = s.pop(), s.pop()
        if i == '+': s.append(a+b)
        elif i == '-': s.append(a-b)
        elif i == '*': s.append(a*b)
        else: s.append(a/b)

    else:#op
        s.append(int(i))

print(s[0])