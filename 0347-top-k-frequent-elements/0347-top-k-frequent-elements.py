class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [i[0] for i in sorted(list(c.items()) , key = lambda x : x[1] ,reverse = True)[:k]]
