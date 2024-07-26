class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        while tickets[k] > 0:
            tmp = tickets[k]
            for i in range(len(tickets)):
                if tickets[i] > 0 and (tmp != 1 or (tmp == 1 and i <= k)) :
                    cnt += 1
                    tickets[i] -= 1
        return cnt
