n = int(input())
w1, w2, h1, h2 = map(int, input().split())
v_in = list(map(int, input().split()))
cur_v, cur_h = 0, 0
v1, v2 = w1**2*h1, w2**2*h2
max_v = w1**2*h1 + w2**2*h2
max_dh = 0

for v in v_in:
    if cur_v + v > max_v: v = max_v - cur_v
    if cur_v < v1:
        if cur_v + v <= v1:
            dh = v // w1**2
        else:
            dh = (h1 - cur_h) + (cur_v+v-v1)//w2**2
    else:
        dh = v // w2**2
    
    if max_dh < dh: max_dh = dh
    cur_h += dh
    cur_v += v

print(max_dh)
