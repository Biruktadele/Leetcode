class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        wind = len(part)
        l = 0
        stuck = []
        for i in range(len(s)):
            stuck.append(s[i])
            if stuck[-wind::] == list(part):
                for _ in range(wind):
                    stuck.pop()
        return "".join(stuck)

        