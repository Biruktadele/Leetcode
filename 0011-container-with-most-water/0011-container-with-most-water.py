class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        mx = 0

        while l < r:
            h1 = height[l]
            h2 = height[r]
            
            mx = max(mx ,min(h1,h2) * (r-l))

            if h1 > h2:
                r -= 1
            else:
                l += 1
        return mx
        