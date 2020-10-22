class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
class CircularLinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size ==0
    
    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()
        
    def addLast(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def addFirst(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            newest._next = newest
            self._head = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1
        
    def addAny(self, e, pos):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < (pos - 1):
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1
        
    def removeFirst(self):
        if self.isEmpty():
            print('CircularList is empty')
            return
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.isEmpty():
            self._head = None
            self._tail = None
        return e
    
    def removeLast(self):
        if self.isEmpty():
            print('CircularList is empty')
            return
        p = self._head
        i = 1
        while i < self._size -1:
            p =p._next
            i += 1
        self._tail = p
        p = p._next
        self._tail._next = self._head
        e = p._element
        self._size -= 1
        return e
    
    def removeAny(self, pos):
        p = self._head
        i = 1
        while i < (pos-1):
            p = p._next
            i += 1
        e = p._next._element    
        p._next = p._next._next
        self._size -=1
        return e
   
  
  
  

  
  if __name__ == '__main__':

    C = CircularLinkedList()
    C.addLast(7)
    C.addLast(4)
    C.addLast(12)
    C.display()
    print('Size:',C._size)
    C.addLast(8)
    C.addLast(3)
    C.display()
    print('Size:',C._size)
    C.addFirst(17)
    C.display()
    print('Size:',C._size)
    C.addAny(125,4)
    C.display()
    print('Size:',C._size)
    print(C.removeFirst(), 'removed')
    C.display()
    print('Size:',C._size)
    print(C.removeLast(), 'removed')
    C.display()
    print('Size:',C._size)
    print(C.removeAny(3), 'removed')
    C.display()
    print('Size:',C._size)
        
        
