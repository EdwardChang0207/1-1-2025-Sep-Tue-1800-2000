class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size
        self.length = 0
        self.top = -1
    def push(self, item):
        if self.length == self.size:
            print('Full')
            return
        self.top += 1
        self.data[self.top] = item
        self.length += 1
    def pop(self):
        if self.length == 0:
            print('Empty')
            return None
        item = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        self.length -= 1
        return item

N = int(input())
while N != 0:
    l = list(map(int, input().split()))
    while l != [0]:
        station = Stack(N)
        train = [i for i in range(1, N+1)]
        f = False
        while l:
            while (l[0] != station.data[station.top]) and train:
                station.push(train.pop(0))
            while l and (l[0] == station.data[station.top]):
                station.pop()
                l.pop(0)
            if not train and l:
                print('No')
                f = True
                break
            if not(l) and not(train) and station.top == -1:
                break
        if not f:
            print('Yes')
        l = list(map(int, input().split()))
        print(l)
    N = int(input())