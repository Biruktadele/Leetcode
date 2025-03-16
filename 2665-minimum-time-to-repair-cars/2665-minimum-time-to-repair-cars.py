class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_can_repair( minute):
            car = 0
            for i in ranks:
                car += int(sqrt(minute // i))
            return cars <= car
        r = max(ranks) * cars**2
    
        return bisect_left(range(r), True, key=is_can_repair)
            