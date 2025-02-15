class MinStack:

    def __init__(self):
        self.stuck = []
        self.minn = []

    def push(self, val: int) -> None:
        self.stuck.append(val)
        if self.minn:
            self.minn.append(min(self.minn[-1] , val))
        else:
            self.minn.append(val)
            
    def pop(self) -> None:
        self.stuck.pop()
        self.minn.pop()
    def top(self) -> int:
        return self.stuck[-1]
    
    def getMin(self) -> int:
        return self.minn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()