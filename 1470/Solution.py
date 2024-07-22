class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        tmp = []
        for i in range(n):
            tmp.append(nums[i])
            tmp.append(nums[i+n])
        return tmp