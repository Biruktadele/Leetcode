class Solution:
    def intersect(self, num1: List[int], num2: List[int]) -> List[int]:
        d = {}
        ans = []
        for i in range(len(num1)):
            if num1[i] not in d:
                d[num1[i]] = 1
            else:
                d[num1[i]] += 1
        for j in num2:
            if j in d:
                if d[j] > 0:
                    d[j] -= 1
                    ans.append(j)
                
        
        # x = set(ans)
        # x = list(x)
        return ans