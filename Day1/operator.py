#Math
'''
+-*/ ** % //
'''
#Relation
'''
==, !=, >, <, >=, <=
'''
#Logical
'''
1.not 反閘
    周杰倫：哎呦不錯喔 -> True
    不(not)錯(False) -> True
    錯 -> False
    不(not)行(True) -> False
    行 -> True

2.or 或閘
    Math or Eng -> 3000
    T.      F.     T
    F.      T.     T
    T.      T.     T
    F.      F.     F

3.and 且閘
    HW and 打掃 -> :)
    T.     F.     F
    F.     T.     F
    T.     T.     T
    F.     F.     F

4.xor(excursive or) 斥或閘
    珍奶 xor 烏龍 -> :)
    T.      F.      T
    F.      T.      T
    T.      T.      F
    F.      F.      F

    [1]not or and
    whitelist and blacklist
    (a or b) and not(a and b)
    [2]binary
'''
a, b = 3, 0
    
print((a or b) and not(a and b))
print(a^b)