class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distance = {}


        for j in range(len(nums)):
            i = nums[j]
            if i not in distance:
                distance[i] = j
            else:
                if abs(distance[i]-j) <= k:
                    return True
                    
                else:
                    distance[i] = j
        return False
        


       