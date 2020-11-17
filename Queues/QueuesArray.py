class QueuesArray:
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def enqueue(self, e):
        self._data.append(e)
    
    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        return self._data.pop(0)
    
    def first(self):
        if self.isEmpty():
            print('Queue is Empty')
            return
        else:
            return self._data[0]    
         
         
         
         
if __name__ == '__main__':
    
    Q = QueuesArray()
    print(Q.isEmpty())
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    print(Q.isEmpty())
    print(len(Q))
    print(Q._data)
    print(Q.dequeue())
    print(Q._data)
    print(Q.first())
    print(len(Q))
    print(Q.isEmpty())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())         
         
