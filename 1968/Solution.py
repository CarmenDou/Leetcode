import math
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i, mid = 0, math.ceil(len(nums)/2)
        while i < mid-1:
            res.append(nums[i])
            res.append(nums[i+mid])
            i += 1
        if len(nums)%2 == 0:
            res.append(nums[i])
            res.append(nums[i+mid])
        else:
            res.append(nums[i])
        return res
