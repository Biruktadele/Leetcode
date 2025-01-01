class Solution:
    def maxScore(self, s: str) -> int:
        s = [int(i) for i in s]
        mx = 0
        for i in range(1,len(s)):
            left = s[0:i].count(0)
            right = s[i::].count(1)
            mx = max(mx , left+right)
        return mx

            
        