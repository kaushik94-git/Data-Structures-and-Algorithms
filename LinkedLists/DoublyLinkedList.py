class _Node:
    
    __slots__ = '_element', '_next', '_prev'
    
    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev
        
        
class DoubleLinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
        
    def __len__(self):
        return self._size
    
    
    def isEmpty(self):
        return self._size == 0
    
    
    def display(self):
        p = self._head
        while p:
            print(p._element, end='==>')
            p = p._next
        print()
        
        
    def displayRev(self):
        p = self._tail
        while p:
            print(p._element, end='==>')
            p = p._prev
        print()
    
    
    def addLast(self, e):
        newest = _Node(e, None, None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1
        
        
    def addFirst(self, e):
        newest = _Node(e, None, None)
        if self.isEmpty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1
        
    def addAny(self, e, pos):
        newest = _Node(e, None, None)
        p = self._head
        i = 1
        while i < (pos -1):
            p = p._next
            i += 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1
        
        
    def removeFirst(self):
        if self.isEmpty():
            print('Empty List')
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return e
            
        
    def removeLast(self):
        if self.isEmpty():
            print('Empty List')
            return
        e = self._tail
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        return e
            
        
    def removeAny(self, pos):
        if self.isEmpty():
            print('Empty List')
            return
        p = self._head
        i = 1
        while i < (pos-1):
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size += 1
        return e
    
    
    
if __name__ == '__main__':

    D = DoubleLinkedList()
    D.addLast(7)
    D.addLast(4)
    D.addLast(12)
    D.display()
    print("Size:", len(D))
    D.addLast(8)
    D.addLast(3)
    D.displayRev()
    print("Size:", len(D))
    D.addFirst(25)
    D.display()
    print("Size:", len(D))
    D.addAny(125,3)
    D.display()
    print("Size:", len(D))
    D.removeFirst()
    D.display()
    print("Size:", len(D))
    D.removeLast()
    D.display()
    print("Size:", len(D))
    D.addLast(3)
    D.display()
    print("Size:", len(D))
    D.removeAny(3)
    D.display()
    print("Size:", len(D))
