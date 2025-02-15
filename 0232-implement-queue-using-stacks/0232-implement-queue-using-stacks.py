class MyQueue:

    def __init__(self):
        self.num = deque([])

    def push(self, x: int) -> None:
        self.num.append(x)        

    def pop(self) -> int:
        return self.num.popleft()
    def peek(self) -> int:
        return self.num[0]
        

    def empty(self) -> bool:
        return not bool(self.num)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()