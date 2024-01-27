class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        i = 1
        while i < n:
            count,j = 1, 1
            tmp = ""
            while j < len(res):
                if res[j-1] <> res[j]:
                    tmp += str(count) + res[j-1]
                    count = 1
                else:
                    count += 1
                j += 1
            tmp += str(count) + res[j-1]
            res = tmp
            i += 1
        return res


        