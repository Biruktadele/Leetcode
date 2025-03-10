class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = []
        i = 0
        while i < len(word1) and i < len(word2):
            l.append(word1[i])
            l.append(word2[i])
            i+= 1

        l += list(word1[i::])
        l += list(word2[i::])
        return "".join(l)

        