class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        avail = [] # [processingTime, index]
        unavail = [(task[0], task[1], index) for index, task in enumerate(tasks)] # [enqueueTime, processingTime, index]
        heapq.heapify(unavail)

        seq = [0] * len(tasks)
        curTime = 0
        for i in range(len(seq)):
            if not avail and curTime < unavail[0][0]:
                curTime = unavail[0][0]
            while unavail and curTime >= unavail[0][0]:
                enqueueTime, processingTime, index = heapq.heappop(unavail)
                heapq.heappush(avail, (processingTime, index))

            processingTime, index = heapq.heappop(avail)
            seq[i] = index
            curTime += processingTime
        return seq
