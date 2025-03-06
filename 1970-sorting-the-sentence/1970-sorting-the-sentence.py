class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = lambda x : x[-1])
        s = [i[:-1:] for i in s]
        return " ".join(s)
        