class _Node:
    
    __slots__ = '_element', '_next'
    
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
class StacksLinked:
    
    def __init__(self):
        self._top = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        else:
            e = self._top._element 
            self._top = self._top._next
            self._size -= 1
            return e
    
    def top(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        return self._top._element
    
    def display(self):
        p = self._top
        while p:
            print(p._element, end = '-->')
            p = p._next
        print()
        
        
        
if __name__ == '__main__':
  S = StacksLinkedList()
  S.push(3)
  S.push(5)
  S.display()
  print(len(S))
  print(S.isEmpty())
  S.pop()
  S.display()
  S.pop()
    print(S.isEmpty())
