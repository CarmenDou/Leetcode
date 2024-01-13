from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = Counter(s)
        i = 0 
        if len(s) != len(t):
            return False

        while i < len(t):
            if t[i] not in dic_s:
                return False
            else:
                dic_s[t[i]] -= 1
                if dic_s[t[i]] < 0:
                    return False
            i += 1
        
        return True
        