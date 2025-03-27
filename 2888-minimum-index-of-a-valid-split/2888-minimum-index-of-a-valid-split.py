class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dicl = defaultdict(int)
        dicr = Counter(nums)

        for i in range(len(nums)):
            dicl[nums[i]] += 1
            dicr[nums[i]] -= 1

            if dicl[nums[i]] > i + 1 - dicl[nums[i]] and dicr[nums[i]] > len(nums) - (i+1) - dicr[nums[i]] :
                return i
        return -1