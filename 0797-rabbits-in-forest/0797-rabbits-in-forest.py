class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        s = 0
        for i in c:
            if i == 0:
                s += c[i]
            else:
                s += (i+1) * math.ceil(c[i]/(i+1))
        return s
        
        