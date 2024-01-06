class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        table = {0:1}
        pre = 0
        for num in nums:
            pre += num
            if pre-k in table:
                res += table[pre-k]
            if pre in table:
                table[pre] += 1
            else:
                table[pre] = 1
        return res
