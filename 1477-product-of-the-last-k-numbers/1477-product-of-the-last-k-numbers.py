class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        self.zero = -1

    def add(self, num: int) -> None:
        
        if num:
            self.nums.append(self.nums[-1]*num)
        else:
            
            self.zero = len(self.nums)
            self.nums.append(1)
            
        
    def getProduct(self, k: int) -> int:
        if len(self.nums) -k-1 < self.zero:
            
            return 0
        return self.nums[-1] // self.nums[-(k+1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)