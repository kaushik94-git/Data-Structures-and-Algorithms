class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addLast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def addFirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1
        
    def addAny(self, e, position):
        if self._size < position:
            return False
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < (position -1):
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1        

    def display(self):
        p = self._head
        while p:
            print(p._element,end=' --> ')
            p = p._next
        print()
        
    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return False
    
    def removeFirst(self):
        if self.isempty():
            print('List is Empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e
    
    def removeLast(self):
        if self.isempty():
            print('List is Empty')
            return
        p = self._head
        i = 1
        while i < (len(self) -1):
            p = p._next
            i += 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1
        
    def removeAny(self,position):
        p = self._head
        i = 1
        while i < (position-1):
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e
    
    
    
    
    
    

if __name__ == '__main__':
    
    
    L = LinkedList()
    print("Size:", len(L))
    L.addLast(7)
    L.addLast(8)
    L.addLast(12)
    L.addLast(4)
    L.addLast(3)
    L.display()
    print("Size: Add Last", len(L))
    print(L.search(3))
    L.addFirst(9)
    L.display()
    print("Size: Add First", len(L))
    L.addAny(126,9)
    L.addAny(125,4)
    L.display()
    print("Size: Add Any", len(L))
    L.removeFirst()
    L.display()
    print("Size: Remove First", len(L))
    L.removeLast()
    L.display()
    print("Size: Remove Last", len(L))
    L.removeAny(2)
    L.display()
    print("Size: Remove Any", len(L))
