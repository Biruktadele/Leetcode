class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = Counter(words)

        single = 0
        c = 0
        # print(dic)
        for i in words:
            
            if dic[i] > 0:
                dic[i] -= 1
                s = i[::-1]
                if s in dic and dic[s] > 0:
                    dic[s] -= 1
                    c += 4
                else:
                    if i[0] == i[1]:
                        single += 1
            
        return c + 2 if single else c
                



        