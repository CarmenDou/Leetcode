class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJumpIndex = 0
        i = 0
        while i <= maxJumpIndex:
            maxJumpIndex = max(maxJumpIndex, nums[i]+i)
            if maxJumpIndex >= len(nums)-1:
                return True
            i += 1
        return False