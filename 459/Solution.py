class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # sub_s = ""
        # for i in range(len(s)-1):
        #     sub_s = sub_s + s[i]
        #     if replace(s,sub_s,"") == "":
        #         return True
        # return False
        if not s:
            return false
        k=2
        while k<=len(s):
            if len(s)%k==0 and s[:len(s)//k]*k==s:
                return True
            k+=1
        return False