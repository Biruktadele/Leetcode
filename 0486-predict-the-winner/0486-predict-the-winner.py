class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(left,right):
            if left > right:
                return 0
            numl = nums[left] -  winner(left+1,right)
            numr = nums[right] -  winner(left,right-1)

            return max(numl , numr)
        return winner(0,len(nums)-1) >= 0
        