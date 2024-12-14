class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        max_deque = deque()  # To maintain the max values in the window
        min_deque = deque()  # To maintain the min values in the window
        l = 0
        total = 0

        for r in range(len(nums)):
            # Update max_deque
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            max_deque.append(r)

            # Update min_deque
            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            min_deque.append(r)

            # Shrink the window if the condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                l += 1
                # Remove indices that are out of the window
                if max_deque[0] < l:
                    max_deque.popleft()
                if min_deque[0] < l:
                    min_deque.popleft()

            # Count valid subarrays ending at r
            total += (r - l + 1)

        return total








        