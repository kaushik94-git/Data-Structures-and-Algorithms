class DEQueueArray:
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def addFirst(self, e):
        self._data.insert(0, e)
        
    def removeFirst(self):
        if self.isEmpty():
            print('DEQueue is Empty')
            return
        return self._data.pop(0)
    
    def First(self):
        if self.isEmpty():
            print('DEQueue is Empty')
            return        
        return self._data[0]
    
    def Last(self):
        if self.isEmpty():
            print('DEQueue is Empty')
            return        
        return self._data[-1]
        
    def addLast(self, e):
        self._data.append(e)
        
    def removeLast(self):
        if self.isEmpty():
            print('DEQueue is Empty')
            return
        return self._data.pop()
    
    
    
if __name__ == "__main__":
    
    DE = DEQueueArray()
    print(DE.isEmpty())
    DE.addFirst(1)
    DE.addFirst(10)
    DE.addLast(2)
    DE.addLast(20)
    print(DE._data)
    print(DE.First())
    print(DE.Last())
    print(DE.removeFirst())
    print(DE.removeLast())
    print(DE._data)
    print(DE.removeFirst())
    print(DE.removeLast())
    print(DE.isEmpty())    
