class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        pair = 0
        non_pair = 0
        for i in c:
            pair += c[i]//2
            non_pair += c[i] %2
        return [pair ,non_pair]

        