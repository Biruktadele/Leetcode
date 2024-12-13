class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        n_c = sorted(nums)
        n_c = deque(n_c)
        d = defaultdict(deque)
        for i , j in enumerate(nums):
            d[j].append(i)
        i = len(nums)
        s = 0
        while i > 0:
            x = n_c.popleft()
            y = d[x].popleft()
            if nums[y] != -1:
                s += nums[y]
                nums[y] = -1
                if y-1 >= 0:
                    nums[y-1] = -1
                if y+1 < len(nums):
                    nums[y+1] = -1
            i -= 1
        return s