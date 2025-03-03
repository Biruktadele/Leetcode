class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        back = 0
        front = 0
        l = len(nums)
        num = nums[:]
        piv = nums.count(pivot)
        while front < l:
            if nums[front] < pivot:
                nums[front], nums[back] = nums[back] , nums[front]
                back += 1
                front += 1
            else:
                front += 1
        back = l-1
        front = l-1

        while front >= 0:
            if num[front] > pivot:
                num[front], num[back] = num[back] , num[front]
                back -= 1
                front -= 1
            else:
                front -= 1
        ans = []
        print(num)
        print(nums)
        b = True
        for i in range(l):
            if b:
                if nums[i] < pivot:
                    ans.append(nums[i])
                else:
                    b = False
                    ans.extend([pivot] * piv)
            else:
                if num[i] <= pivot:
                    continue
                else:
                    ans.append(num[i])
        return ans
        