class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        dic = defaultdict(int)
        ln = len(s)
        res = 0
        for r in range(ln):
            if s[r] in "abc":
                dic[s[r]] += 1
            while len(dic) == 3:
                res += ln - r
                if s[l] in dic:
                    dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    dic.pop(s[l])
                l += 1
        return res

        