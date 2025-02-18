class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # postion_passengers = [0]*1001
        # for trip in trips:
        #     numPassengers, from_postion, to_postion = trip[0], trip[1], trip[2]
        #     for p in range(from_postion, to_postion):
        #         postion_passengers[p] += numPassengers
        #         if postion_passengers[p] > capacity:
        #             return False
        # return True

        trips.sort(key = lambda t: t[1])

        minHeap = [] # pair of [end, numPassengers]
        curPass = 0
        for t in trips:

            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)

            curPass += numPass
            if curPass > capacity:
                return False
            
            heapq.heappush(minHeap, [end, numPass])
        return True