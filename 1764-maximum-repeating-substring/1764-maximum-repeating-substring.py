class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l = 0
        c = 0
        maxx = 0
        for r in range(len(sequence)):
            l = r
            j = 0
            while l < len(sequence) and word[j] == sequence[l]:
                j += 1
                l += 1
                if j == len(word):
                    c += 1
                    j = 0
            maxx = max(maxx , c)
            c = 0
        return maxx
