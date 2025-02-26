class SeatManager:

    def __init__(self, n: int):
        self.seats = [ i for i in range(1, n+1)]
        heapq.heapify(self.seats)
        return None

    def reserve(self) -> int:
        return heapq.heappop(self.seats)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        return None


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)