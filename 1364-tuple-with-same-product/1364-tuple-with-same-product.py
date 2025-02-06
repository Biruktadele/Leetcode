class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product[nums[i]*nums[j]] += 1
        s = 0
        for i in product:
            if product[i] > 1:
                s += (product[i]*(product[i]-1))  * 4
     
        return s

 