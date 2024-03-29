# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        small = 0
        large = n+1
        while small <= large:
            mid = small + (large-small)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                small = mid
            elif guess(mid) == -1:
                large = mid
            else:
                pass
        return -1

################################        
        left,right=1,n
        mid=left
        while left<=right:
            mid=left+(right-left)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res==1:
                left=mid+1
            elif res==-1:
                right=mid-1
        
        return mid