# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         minLength = inf
#         for i in range(len(nums)) :
#             sum = 0
#             length = 0
#             for j in range(i,len(nums)):
#                 sum += nums[j]
#                 length += 1
#                 if sum >= target and minLength > length :
#                     minLength = length
#                     break
#         if minLength == inf :
#             minLength = 0
#     return minLength

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cum = 0
        first = 0
        last = 0
        count = len(nums)
        if sum(nums) < target:
            return 0
        else:
            while last < len(nums) :
                while cum < target and last < len(nums):
                    cum += nums[last]
                    last += 1
                while cum >= target:
                    cum -= nums[first]
                    first += 1
                count = min(count, last-first+1)
            return count
