class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # return s == s[::-1]

        s = str(x)
        low, high = 0, len(s)-1
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True 

        