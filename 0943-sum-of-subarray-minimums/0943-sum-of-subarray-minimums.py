class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] #[org,chang , val]
        s = 0
        for i, val in enumerate(arr):
            if not stack:
                stack.append([i,i,val])
            else:
                ind = i
                while stack and stack[-1][2] > val:
                    
                    org , chg, num = stack.pop()
                    ind = chg
                    s += (org-chg+1) * num * (i-org)
                
                
                stack.append([i,ind,val])
        l = len(arr)
        # print(stack)
        for i in stack:
            org , chg, num = i
            s += (org-chg+1) * num * (l-org)
        return s % (10**9+7)
