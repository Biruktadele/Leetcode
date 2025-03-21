class RandomizedSet:

    def __init__(self):
        self.num = {}
        self.d = []
        
    def insert(self, val: int) -> bool:
        if val in self.num:
            return False
        self.num[val] = len(self.d)
        self.d.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.num:

            
            self.num[self.d[-1]] = self.num[val]
            self.d[-1] , self.d[self.num[val]] = self.d[self.num[val]] , self.d[-1]

            self.d.pop()
            del self.num[val]

            return True
            
        return False

    def getRandom(self) -> int:
        import random
        x = random.randint(0,len(self.d)-1)
        return self.d[x]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()