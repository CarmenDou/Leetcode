class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution1
        len_nums = len(nums)
        res = [1] *len_nums
        pre, post = 1, 1
        prefix, postfix = [1] *len_nums, [1] *len_nums
        for i in range(len_nums):
            prefix[i] = pre
            pre *= nums[i]
        for i in range(len_nums-1,-1,-1):
            postfix[i] = post
            post *= nums[i]

        for i in range(len_nums):
            res[i] = prefix[i]*postfix[i]

        return res

        # Solution2
        len_nums = len(nums)
        res = [1] * (len_nums)

        prefix, postfix = 1, 1
        for i in range(len_nums):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res 