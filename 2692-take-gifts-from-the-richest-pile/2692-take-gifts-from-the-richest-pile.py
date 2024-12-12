class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #[10,8,5,9,4]
        for i in range(k):
            Mx = max(gifts)
            j = gifts.index(Mx)
            gifts[j] = int(sqrt(Mx))
        return sum(gifts)