class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        buy = 0
        i = 0

        while i< len(costs) and costs[i] <= coins:
            coins -= costs[i]
            i += 1
            buy += 1

        return buy

        