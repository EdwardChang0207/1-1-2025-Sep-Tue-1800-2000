s = input().strip()

def cut(exp, ch):
    arr = []
    level = 0
    start = 0

    for i, c in enumerate(exp):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        elif c == ch and level == 0:
            arr.append(exp[start:i])
            start = i + 1
    
    arr.append(exp[start:])
    return arr

def mul(exp):
    parts = cut(exp, '*')

    ans = 1
    for p in parts:
        ans *= add(p)

    return ans

def add(exp):
    parts = cut(exp, '+')

    ans = 0
    for p in parts:
        ans += val(p)

    return ans

def val(exp):
    # 純數值
    if exp[0].isdigit():
        return int(exp)

    # f()
    insides = exp[2:-1]
    args = cut(insides, ',')

    nums = []
    for x in args:
        nums.append(mul(x))

    return max(nums) - min(nums)


# mul -> add -> val
print(mul(s))