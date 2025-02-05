class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for i in accounts:
            user = sum(i)
            mx = max(user,mx)
        return mx
        