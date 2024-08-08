class UndergroundSystem:

    def __init__(self):
        self.checkInAndOut = {}
        self.stationRecord = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInAndOut[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInAndOut[id]
        del self.checkInAndOut[id]
        if (startStation, stationName) not in self.stationRecord:
            self.stationRecord[(startStation, stationName)] = []
        self.stationRecord[(startStation, stationName)].append(t - startTime)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stationRecord[(startStation, endStation)])/len(self.stationRecord[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)