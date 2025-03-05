class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.stack = []
        self.size = k
        

    def consec(self, num: int) -> bool:
        if self.val != num:
            self.stack = []
            return False
        else:
            self.stack.append(num)
            if len(self.stack) >= self.size:
                return True
            else:
                return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)