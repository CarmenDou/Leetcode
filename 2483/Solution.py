class Solution:
    def bestClosingTime(self, customers: str) -> int:
        hour, minPenalty = 0, float('inf')
        yCnt, nCnt = 0, 0
        for customer in customers:
            if customer == "Y":
                yCnt += 1

        i = 0
        while i < len(customers)+1:
            if yCnt+nCnt < minPenalty:
                hour = i
                minPenalty = min(minPenalty, yCnt+nCnt)
            if i < len(customers):
                if customers[i] == "Y":
                    yCnt -= 1
                else:
                    nCnt += 1
            i += 1
        return hour