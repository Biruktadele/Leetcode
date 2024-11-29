class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        left_profit = [0] * n  
        right_profit = [0] * n 


        Min = prices[0]
        for i in range(1, n):
            Min = min(Min, prices[i])
            left_profit[i] = max(left_profit[i-1], prices[i] - Min)


        Max = prices[-1]
        for i in range(n-2, -1, -1):
            Max = max(Max, prices[i])
            right_profit[i] = max(right_profit[i+1], Max - prices[i])
        Max = 0
        for i in range(n):
            Max = max(Max, left_profit[i] + right_profit[i])

        return Max