class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # new_nums = nums + nums
        # print(new_nums)

        # stack = []
        # dic = {}
        # for key,num in enumerate(new_nums):
        #     if not stack:
        #         stack.append(key)
        #     else:
        #         while stack and new_nums[stack[-1]] < num:
        #             dic[stack[-1]] = key
        #             stack.pop()
        #         stack.append(key)
        # while stack:
        #     dic[stack[-1]] = -1
        #     stack.pop()

        # res = []
        # for key in range(len(nums)):
        #     if dic[key] != -1:
        #         res.append(new_nums[dic[key]])
        #     else:
        #         res.append(-1)
        # return res

        # stack = []
        # new_nums = nums + nums
        # next_large = [-1] * len(new_nums)
        # for key,num in enumerate(new_nums):
        #     if not stack:
        #         if key <= len(new_nums)/2:
        #             stack.append(key)
        #         else:
        #             break
        #     else:
        #         while stack and new_nums[stack[-1]] < num:
        #             next_large[stack[-1]] = num
        #             stack.pop()
        #         stack.append(key)

        # return next_large[:len(nums)]

# we can use mod to get the index of the circular list and cycling twice.
# 循环数组，通过余数进行索引，把数组扩大两倍     
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)*2):
            while stack and nums[stack[-1]] < nums[i%len(nums)]:
                index = stack.pop()
                res[index] = nums[i%len(nums)]
            stack.append(i%len(nums))
        return res
