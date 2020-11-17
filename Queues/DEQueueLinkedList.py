class _Node:
    
    __slots__ = '_element', '_next'
    
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        

class DEQueueLinkedList:
    
    
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
        
        
    def __len__(self):
        return self._size
    
    
    def isEmpty(self):
        return self._size == 0
    
    
    def addFirst(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1
        
    
    def removeFirst(self):
        if self.isEmpty():
            print('Dequeue is Empty')
            return
        else:
            e = self._front._element
            self._front = self._front._next
            self._size -= 1
            if self.isEmpty():
                self._rear = None
            return e
        
    
    def First(self):
        if self.isEmpty():
            print('Dequeue is Empty')
            return        
        return self._front._element
    
    
    def Last(self):
        if self.isEmpty():
            print('Dequeue is Empty')
            return        
        return self._rear._element
    
    
    def addLast(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1
        

    def removeLast(self):
        if self.isEmpty():
            print('Dequeue is Empty')
            return
        p = self._front
        i = 1
        while i < (len(self) - 1):
            p = p._next
            i += 1
        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size -= 1
        return e
        

    def display(self):
        p = self._front
        while p:
            print(p._element , end='==>' )
            p = p._next
        print()
        
if __name__ == "__main__":
    
    DE = DEQueueLinkedList()
    print(DE.isEmpty())
    DE.addFirst(1)
    DE.addLast(10)
    DE.display()
    print(DE.removeLast())
    DE.display()
    DE.addFirst(2)
    DE.addLast(0)
    DE.display()
    DE.addLast(-1)
    DE.addLast(-2)
    print(DE.First())
    print(DE.Last())
    DE.display()
    print(DE.removeLast())
    print(DE.removeFirst())
    DE.display()
            
        
        
        
        
