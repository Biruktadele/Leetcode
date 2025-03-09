class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-int(i) for i in stones]
        heapq.heapify(stones)
        while len(stones) != 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            heapq.heappush(stones, x-y)
        return -heapq.heappop(stones)