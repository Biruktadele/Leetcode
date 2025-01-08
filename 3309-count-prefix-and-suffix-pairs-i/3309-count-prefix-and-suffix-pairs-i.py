class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                l = len(words[i])
                
                if len(words[j]) >= l and words[i] == words[j][0:l] and words[i] == words[j][len(words[j]) - l::]:
                    c += 1
        return c
        