class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def sumEven(num):
            s = 0
            for i in num:
                if i % 2 == 0:
                    s += i
            return s
        s = sumEven(nums)
        ans = []
        for i in queries:
            org = nums[i[1]]
            nums[i[1]] += i[0]
            if org % 2:
                if nums[i[1]] % 2 == 0:
                    s += nums[i[1]]
            else:
                if nums[i[1]] % 2:
                    s -= org
                else:
                    s += i[0]
            ans.append(s)
        return ans
            

        