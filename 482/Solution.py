class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        tmp_str = s.replace("-","").upper()
        len_s = len(tmp_str)
        n = len_s % k
        m = 0
        res = ""
        if n != 0 :
            res = tmp_str[:n]
            m += n
        while m < len_s:
            res = res + "-" + tmp_str[m:m+k]
            m += k
        if n == 0 :
            res = res[1:]
        return res
