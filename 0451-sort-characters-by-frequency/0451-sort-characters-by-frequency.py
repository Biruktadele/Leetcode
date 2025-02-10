class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sor = sorted(c.items(), key=lambda x: x[1],reverse = True)
       
        ans = []
        for i in sor:
            ans.append(i[0]*i[1])
        return "".join(ans)
        