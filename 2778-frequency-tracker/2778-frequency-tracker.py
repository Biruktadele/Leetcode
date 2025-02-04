class FrequencyTracker:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.chake = defaultdict(int)
        

    def add(self, number: int) -> None:
        if self.chake[self.frequency[number]]:
            self.chake[self.frequency[number]] -= 1
        self.frequency[number] += 1
        self.chake[self.frequency[number]] += 1
        

    def deleteOne(self, number: int) -> None:
        
        if self.frequency[number]:
            self.chake[self.frequency[number]] -= 1
            self.frequency[number] -= 1
            self.chake[self.frequency[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return bool(self.chake[frequency])
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)