class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        profit = 0
        i = 0
        l = len(prices)
        while i < l:
            while i < l-1 and prices[i] > prices[i+1]:
                i += 1
            buy = prices[i]
            i += 1
            while i < l and prices[i-1] < prices[i]:
                i += 1
            
            sell = prices[i-1]
            if sell - buy > 0:
                profit += sell - buy
        return profit