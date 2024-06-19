class Solution:
    def jump(self, nums: List[int]) -> int:
        preMax, i = 0, 0
        cnt, nextMax = 0, 0
        while i < len(nums)-1:
            nextMax = max(nextMax, nums[i]+i)
            if i == preMax:
                preMax = nextMax
                cnt += 1
            i += 1 
        return cnt