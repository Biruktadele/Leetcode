class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        s = 0
        for i in words:
            d = Counter(i)
            for j in d:
                if j not in c or d[j] > c[j]:
                    break
            else:
                s += len(i)
        return s

        