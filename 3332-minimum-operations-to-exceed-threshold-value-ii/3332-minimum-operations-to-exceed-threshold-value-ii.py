class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            threshold = (min(x,y) * 2 ) + max(x,y)

            heapq.heappush(nums,threshold)
            count += 1
        return count


        