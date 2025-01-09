class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c = 0
        l = len(pref)
        for i in words:
            if i[0:l] == pref:
                c += 1
        return c
        