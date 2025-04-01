class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)

        for i in range(len(questions)-1,-1,-1):
            m = questions[i][1]+1
            if i + m >= len(questions):
                m = 0
            dp[i] = max(questions[i][0] + dp[i + m],dp[i+1])
            
        return dp[0]