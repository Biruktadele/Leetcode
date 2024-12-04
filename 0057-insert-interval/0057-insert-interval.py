class Solution:
    def insert(self, s: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = 0
        po1 = 0
        if len(s) == 0 :
            return [newInterval]
        if len(newInterval) == 0:
            return s 
        if newInterval[0] > s[-1][1]:
            return (s+[newInterval])
        elif newInterval[1] < s[0][0]:
            return ([newInterval] + s)
        while l < len(s):
            if (newInterval[0] <= s[l][0] or newInterval[0] == s[l][1]
            or newInterval[0] in range(s[l][0],s[l][1])):
                po1 = l
                break
            elif l > 0 and newInterval[0] in range(s[l-1][1],s[l][0]):
                po1 = l
                break
            l += 1
        r = len(s)-1
        po2 = 0
        while r > 0:
            if (newInterval[1] >= s[r][0] or newInterval[1] >= s[r][1]
            or newInterval[1] in range(s[r][0],s[r][1])):
                po2 = r
                break
            elif r < len(s)-1 and newInterval[1] in range(s[r-1][1],s[r][0]):
                po2 = r-1
                break
            r -= 1

        x = min(newInterval[0],s[po1][0])
        y = max(newInterval[1],s[po2][1])
        s = s[0:po1]+[[x,y]]+s[po2+1:]
        return s
