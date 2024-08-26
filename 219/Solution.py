class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictNum = {}
        for i, num in enumerate(nums):
            if num in dictNum and (i - dictNum[num]) <= k:
                return True
            dictNum[num] = i
        return False
