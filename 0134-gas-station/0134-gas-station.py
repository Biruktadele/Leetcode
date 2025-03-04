class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num = []
        if sum(gas) < sum(cost):
            return -1
        for i,j in zip(gas,cost):
            num.append(i-j)
        ind = 0
        s = 0
        for i in range(len(num)):
            s += num[i]
            if s < 0:
                s = 0
                ind = i+1
        return ind
            

        