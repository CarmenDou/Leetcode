class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            t1 = low/2
        else:
            t1 = (low-1)/2
        
        if high % 2 == 0:
            t2 = high/2
        else:
            t2 = (high+1)/2
        return int(t2-t1)