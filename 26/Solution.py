class Solution():
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for x in nums:
            bCanAppend = True
            for y in res:
                if x ^ y == 0 :
                    bCanAppend = False
            if bCanAppend :
                res.append(x)
        
        return res
        
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
