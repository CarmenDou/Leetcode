class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_l = 0
        count_a = 0
        max_l = 0
        i = 0
        while i < len(s):
            if s[i] == "A":
                count_a += 1
            if s[i] == "L":
                count_l += 1
            else:
                count_l = 0
            max_l = max(count_l,max_l)  
            i += 1
        if count_a < 2 and max_l < 3:
            return True
        else:
            return False  