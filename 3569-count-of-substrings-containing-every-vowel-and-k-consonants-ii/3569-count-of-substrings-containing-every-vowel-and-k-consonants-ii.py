class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atlistk(k):
            vowel = defaultdict(int)
            res = 0
            cons = 0
            l = 0

            for i in range(len(word)):
                if word[i] in "aeiou":
                    vowel[word[i]] += 1
                else:
                    cons += 1
                
                while len(vowel) == 5 and cons >= k:
                    res += (len(word) - i)
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                    else:
                        cons -= 1 
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1
            return res
        return atlistk(k) - atlistk(k+1)
                    