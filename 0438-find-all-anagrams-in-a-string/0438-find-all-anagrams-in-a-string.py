class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        dictp = {}
        window= {}
        for i in p:
            if i not in dictp:
                dictp[i] = 1
                window[i] = 0
            else:
                dictp[i] += 1
        l = 0
        r = 0
        ans = []
        while r < len(s):
            if s[r] in dictp:
                window[s[r]] += 1
            else:
                for i in dictp:
                    window[i] = 0
                l = r+1
                r = r+1
                continue
            if window[s[r]] > dictp[s[r]]:

                while window[s[r]] > dictp[s[r]] and l <= r:
                    window[s[l]] -= 1
                    l += 1
            if window == dictp:

                ans.append(l)
                window[s[l]] -= 1
                l += 1
                r += 1
                continue
            r += 1
        return ans
