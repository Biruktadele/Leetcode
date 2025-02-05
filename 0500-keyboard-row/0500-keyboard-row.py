class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s = set(list("qwertyuiop"))
        s1 = set(list("asdfghjkl"))
        s2 = set(list("zxcvbnm"))
        ans = []
        for i in words:
            c = 0
            b = False
            k = i
            i = i.lower()
            for j in i:
                if j in s:
                    c += 1
                    b = True
                elif j in s1:
                    c -= 1
                    b = True
            if abs(c) == len(i) or not b:
                ans.append(k)
        return ans