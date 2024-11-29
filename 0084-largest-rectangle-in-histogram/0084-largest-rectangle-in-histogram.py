class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stuck = []
        mx = 0
        for i, height in enumerate(heights):
            if stuck and stuck[-1][0] > height:
                count = i
                while stuck and stuck[-1][0] > height:
                    h, l = stuck.pop()
                    mx = max(mx ,(i-l)*h)
                    count = l
                stuck.append((height,count))
            else:
                stuck.append((height,i))
        l = len(heights)
        for i in range(len(stuck)):
            mx = max(stuck[i][0] * (l-stuck[i][1]) , mx)
           
        return mx
