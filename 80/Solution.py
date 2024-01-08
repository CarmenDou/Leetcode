class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # pre_num = float('inf')
        # pivot_index = -1
        # k = 0
        # for index,num in enumerate(nums):
        #     if pre_num <> num:
        #         pre_num = num
        #         count = 1
        #         k += 1
        #     else:
        #         count += 1
        #         if count > 2:
        #             if pivot_index == -1:
        #                 pivot_index = index
        #         else:
        #             k += 1

        #     if pivot_index <> -1 and count <= 2:
        #         nums[pivot_index] = nums[index]
        #         pivot_index += 1

        # return k

        count,j = 1,1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
                
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j