class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = arr[0]
        chunks = 0
        for i in range(len(arr)):
            mx = max(mx , arr[i])
            if i == mx:
                chunks += 1
        return chunks 
