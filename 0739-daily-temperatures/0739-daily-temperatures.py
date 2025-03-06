class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0]*l
        stack = []

        for j , i in enumerate(temperatures):
            if not stack or stack[-1][1] >= i:
                stack.append([j,i])
            else:
                while stack and stack[-1][1] < i:
                    ans[stack[-1][0]] = j - stack[-1][0] 
                    stack.pop()
                stack.append([j,i])
        return ans
            
        