class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1, diff2 = set(), set()
        for num in nums1:
            if num not in nums2:
                diff1.add(num)

        for num in nums2:
            if num not in nums1:
                diff2.add(num)

        return [list(diff1), list(diff2)]