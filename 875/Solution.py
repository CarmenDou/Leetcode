import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low, high = math.ceil(sum(piles)/h), piles[-1]
        def cntHour(speed):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile/speed)
            return cnt

        while low <= high:
            if cntHour(low) <= h:
                return low

            mid = (low+high)//2
            low += 1
            if cntHour(mid) <= h:
                high = mid
            else:
                low = max(mid + 1, low)

        return mid