class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        word = [set(i) for i in words]
        ans = []
        for i in range(len(word)):
            if x in word[i]:
                ans.append(i)
        return ans