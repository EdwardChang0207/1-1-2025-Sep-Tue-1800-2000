a, b, c = sorted(map(int, input().split()))#sorted -> 排序後的結果（原本的不改變）
print(a, b, c)
if a+b <= c: print('No')
else:
    if a**2+b**2 > c**2:
        print('Acute')
    elif a**2+b**2 == c**2:
        print('Right')
    else:
        print('Obtuse')
