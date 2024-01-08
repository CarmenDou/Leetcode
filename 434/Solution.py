class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # arr = s.split(" ")
        # count = 0
        # for s in arr:
        #     if s != " " and s != "":
        #         count += 1
        # return count
        
        return(len(s.split()))