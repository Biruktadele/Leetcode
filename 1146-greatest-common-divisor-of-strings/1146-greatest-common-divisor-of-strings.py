class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        for i,val in enumerate(str2):
            ans = str1.count(str2[:i+1])
            val = str2.count(str2[:i+1])

            if ans * (i+1) == len(str1) and val * (i+1) == len(str2):
                res = str2[:i+1]
        return res
        