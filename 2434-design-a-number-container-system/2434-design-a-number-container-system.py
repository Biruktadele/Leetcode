class NumberContainers:

    def __init__(self):      
        self.contin = defaultdict(int)
        self.num = defaultdict(SortedSet)
    def change(self, index: int, number: int) -> None:
        if index  in self.contin:
            self.num[self.contin[index]].remove(index)
            if len(self.num[self.contin[index]]) == 0:
                del self.num[self.contin[index]]
            self.num[number].add(index)
            self.contin[index] = number
        else:
            self.contin[index] = number
            self.num[number].add(index)
    def find(self, number: int) -> int:
        if number in self.num:
            return self.num[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)