class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = -1
        base = sum(nums)
        i = 0
        while i < len(nums)-2:
            if base - nums[i] > nums[i]:
                return base
            base -= nums[i]
            i += 1
        return res