class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_can_repair(ranks , minute):
            cars = 0
            for i in ranks:
                cars += int(sqrt(minute // i))
            return cars

        l = 0 
        r = max(ranks) * cars**2
        
        while r > l:
            mid = (l+r)// 2
     
            if is_can_repair(ranks , mid) >= cars:
                r = mid
            else:
                l = mid+1
        return l
            