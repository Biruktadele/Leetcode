class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = "1"*len(nums)
        n = int(n,2)
        # print(n)
        ans = []
        for i in range(n+1):
            t = bin(i)[2:]
            t = t[::-1]
            res = []
            for i in range(len(nums)):
                if i < len(t) and t[i] == "1":
                    res.append(nums[i])
            ans.append(res)
        return ans


        


        