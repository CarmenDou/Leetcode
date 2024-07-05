class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictCnt = Counter(nums)
        cntPairs = 0
        for key, value in dictCnt.items():
            cntPairs += (value-1) * value / 2
        return int(cntPairs)