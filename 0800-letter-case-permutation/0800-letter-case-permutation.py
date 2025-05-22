class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        n = (1 << (len(s)))
        print(n)
        for i in range(n):
            res = []
            for j in range(len(s)):
                if i & (1 << j):
                    res.append(s[j].upper())
                else:
                    res.append(s[j].lower())
            ans.add("".join(res))
        return list(ans)

