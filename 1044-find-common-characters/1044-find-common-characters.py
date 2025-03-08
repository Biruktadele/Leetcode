class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])
        for i in words:
           
            c = Counter(i)
            for i in c:
                dic[i] = min(dic[i] , c[i])
            for i in dic:
                dic[i] = min(dic[i] , c[i])
        ans = []
        print(dic)
        for i in dic:
            if dic[i] > 0:
                ans += [i] * dic[i]
                
        return ans
