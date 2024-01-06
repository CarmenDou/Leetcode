class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res = []
        # for num1 in nums1:
        #     if num1 in nums2 and num1 not in res:
        #         res.append(num1)
        # return res

        # We use '&' to judge whether the two lists have the same value and return the same values in both of the two lists.
        return (nums1 & nums2)

        