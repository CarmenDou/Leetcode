class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # i = 0
        # while i <= x:
        #     if i*i <= x and (i+1)*(i+1) > x:
        #         return i
        #     i += 1

        # 二分查找的思想
        low = 0
        high = x
        while low <= high:
            mid = (low+high)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    low = mid+1
            elif mid*mid > x:
                if (mid-1)*(mid-1) < x:
                    return mid-1
                else:
                    high = mid-1

        