class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        # """
        # i,j = 0, 0
        # p,q = 0, 0
        # while i < m and j < n:
        #     if nums1[p] <= nums2[q]:
        #         i += 1
        #         p += 1
        #     else:
        #         tmp = len(nums1)-2
        #         while tmp >= p:
        #             nums1[tmp+1] = nums1[tmp]
        #             tmp -= 1
        #         nums1[p] = nums2[q]
        #         p += 1
        #         q += 1
        #         j += 1
        # while j < n:
        #     nums1[p] = nums2[q]
        #     p += 1
        #     q += 1
        #     j += 1
        # return None
        while n>0:
            if m<=0 or nums2[n-1]>=nums1[m-1]:
                nums1[m+n-1]=nums2[n-1]
                n=n-1
            else:
                nums1[m+n-1]=nums1[m-1]
                m=m-1

        