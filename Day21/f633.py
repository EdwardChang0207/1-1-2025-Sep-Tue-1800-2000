def face(i):
    f = [[i,i],
         [i,i]]
    return f

b = [
    ['',face(3)],
    [face(5),face(1),face(2),face(6)],
    ['',face(4)]
]

def rotate(face:list):
    new = []
    for i in range(len(face[0])):
        r = []
        for j in range(len(face)):
            r.append(face[j][i])
        new.append(r)
    for i in range(len(new)):
        new[i].reverse()
    return new

def r1(b):
    right = b[1][2]
    b[1][2] = rotate(right)
    col = [b[1][3][0][1],b[1][3][1][1]]
    for i in range(3):
        t = [b[3-i-1][1][0][1],b[3-i-1][1][1][1]]
        b[3-i-1][1][0][1], b[3-i-1][1][1][1] = col[0],col[1]
        col = t
    b[1][3][0][1], b[1][3][1][1] = col[0], col[1]
    return b
def r2(b):
    top = b[0][1]
    b[0][1] = rotate(top)
    # b[1][0][0] -> b[1][1][0] -> b[1][2][0]
    r = b[1][3][0]
    for i in range(4):
        t = b[1][i][0]
        b[1][i][0] = r
        r = t
    return b
def r3(b):
    left = b[1][0]
    b[1][0] = rotate(left)
    col = [b[1][3][0][0],b[1][3][1][0]]
    for i in range(3):
        t = [b[i][1][0][0],b[i][1][1][0]]
        b[i][1][0][1], b[i][1][1][1] = col[0],col[1]
        col = t
    b[1][3][0][0], b[1][3][1][0] = col[0], col[1]
    return b
# def r4(b):

def show(b):
    print('back')
    print(*b[0][1],sep='\n')
    print('left')
    print(*b[1][0],sep='\n')
    print('top')
    print(*b[1][1],sep='\n')
    print('right')
    print(*b[1][2],sep='\n')
    print('bottom')
    print(*b[1][3],sep='\n')
    print('front')
    print(*b[2][1],sep='\n')
b = r1(b)
show(b)

def main():
    import sys
    for i in sys.stdin:
        if i == '1':
        elif i == '2':