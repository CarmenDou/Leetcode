class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # list_s = s.split()
        # res = ""
        # for word in list_s:
        #     res = res + " " + word[::-1]
        # return res[1:]

        i=len(s)-1
        res = []
        word = ""
        while i >= 0:
            if s[i] != " ":
                word += s[i] 
            else:
                res.insert(0,word)
                res.insert(0," ")
                word = ""
            i -= 1
        if word != "":
            res.insert(0,word)
        return "".join(res)