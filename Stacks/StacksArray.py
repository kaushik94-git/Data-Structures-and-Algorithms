class StacksArray:
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        return self._data.pop()
    
    def top(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        return self._data[-1]
    
    def display(self):
        print(self._data)
        return
        
        
        
if __name__ == "__main__":
    S = StacksArray()
    S.push(5)
    S.push(3)
    S.display()
    print(S.isEmpty())
    print(S.pop())
    print(S.isEmpty())
    print(S.pop())
    print(S.isEmpty())
