class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:

        if not self.small:
            heappush(self.small , -num)
        elif num <= -self.small[0]:
            heappush(self.small , -num)
            if len(self.small) > len(self.large):
                val =  - heappop(self.small)
                heappush(self.large , val)
            
        else:
            heappush(self.large , num)
            if len(self.small) < len(self.large):
                val = heappop(self.large)
                heappush(self.small ,  -val)
            
    

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return -self.small[0]



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()