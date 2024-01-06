class Solution():
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums :
            print(x)
            if x % 2 == 0 :
                res.append(nums.pop(x))
        res.extend(nums)
        return res

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))
         