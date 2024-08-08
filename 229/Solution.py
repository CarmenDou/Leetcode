import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        times = math.floor(len(nums)/3)
        res = []
        for key, value in count.items():
            if value > times:
                res.append(key)
        return res