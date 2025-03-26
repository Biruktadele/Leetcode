class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.maxx = []
        self.time = times
        num = -1
        dic = defaultdict(int)
        for i in persons:
            dic[i] += 1
            if num == -1 or dic[num] <= dic[i]:
                num = i
            self.maxx.append(num)
        
    def q(self, t: int) -> int:
        ind = bisect.bisect_left(self.time ,t )
        if ind >= len( self.time) or  self.time[ind] != t:
            ind -= 1
        return self.maxx[ind]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)