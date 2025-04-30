class SeatManager:

    def __init__(self, n: int):
        self.unreservel = [i for i in range(1 ,n+1)]
        heapq.heapify(self.unreservel)
        # self.reserve = set()
    def reserve(self) -> int:
        val = heapq.heappop(self.unreservel)
        # self.reserve.add(val)
        return val

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreservel, seatNumber)


        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)