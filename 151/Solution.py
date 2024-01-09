class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = ""
        for i in range(len(words)-1,-1,-1):
            res = res + " " + words[i]
        return res[1:]

        