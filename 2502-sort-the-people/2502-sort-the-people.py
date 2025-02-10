class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ln = len(heights)
        c = Counter(heights)
        d = {}
        for i in range(len(heights)):
            d[heights[i]] = names[i]

        m = max(c)
        ans= []
        for i in range(m,-1,-1):
            if i in c:
                ans.append(d[i])
      
        return ans



        


        
        return names