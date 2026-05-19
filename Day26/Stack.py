class Stack:
    def __init__(self, size):
        self.size = size
        self.data = ['']*size
        self.top = -1
    
    def push(self, item):
        if self.top == self.size-1:
            print('Full')
            return
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.top == -1:
            print('Empty')
            return None
        item = self.data[self.top]
        self.top -= 1
        return item

s = Stack(5)
s.push(1)
print(f'data:{s.data}, top:{s.top}')
s.push(2)
print(f'data:{s.data}, top:{s.top}')
s.push(3)
print(f'data:{s.data}, top:{s.top}')
item = s.pop()
print(f'data:{s.data}, top:{s.top}, item:{item}')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new = Node(item)
        if not self.top:
            self.top = new
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        item = self.top.data
        self.top = self.top.next
        return item

s = Stack()
s.push(1)
s.push(2)
s.push(3)

def traverse(node):
    while node:
        print(node.data)
        node = node.next

traverse(s.top)
item = s.pop()
print(f'item:{item}')
traverse(s.top)

#stack permutation