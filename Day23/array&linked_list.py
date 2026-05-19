'''
class Array:
    def __init__(self, size):
        self.size = size
        self.data = ['']*size
    def insert(self, item):
        for i in range(self.size):
            if not self.data[i]: 
                self.data[i] = item
                return
        print('Full')
        return
    def pop(self, idx):
        if self.data[idx]:
            r = self.data[idx] 
            self.data[idx] = ''
            return r
        else: return None
    def delete(self, item):
        for i in range(self.size):
            if self.data[i] == item:
                self.data[i] = ''
                return
        print('Not found')
    
a = Array(3)
a.data[1] = 1
print(a.data)
a.insert(2)
print(a.data)

a.insert(3)
print(a.data)

a.insert(4)
print(a.data)

b = a.pop(1)
print(b, a.data)

a.delete(5)
print(a.data)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new
    def pop(self):
        if not self.head:
            print('Empty')
            return
        if not self.head.next:
            r = self.head.data
            self.head = None
            return r
        node = self.head
        while self.next.next:
            node = node.next
        r = node.next.data
        node.next = None
        return r
    def insert(self, idx, data):
        new = Node(data)
        node = self.head
        i = 0
        while (i < idx) and (node):
            prev = node
            node = node.next
            i += 1
        if not(node):
            print('Error')
            return
        prev.next = new
        new.next = node
        
    def remove(self, item):
        node = self.head
        while (node) and (node.data != item):
            prev = node
            node = node.next
        if not(node):
            print('Error')
            return
        prev.next = node.next

# a -> b -> a -> b
#a -> b -> c
l = LinkedList()
l.head = Node('a')
l.head.next = Node('b')
l.head.next.next = Node('c')

l.insert(1, 'd')
l.remove('b')

def traverse(node):
    if node:
        print(node.data)
        traverse(node.next)
traverse(l.head)