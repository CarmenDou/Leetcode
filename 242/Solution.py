from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution1
        list_s = sorted(s)
        list_t = sorted(t)
        return list_s == list_t


        # Solution2
        if len(s) != len(t):
            return False
        
        countS, countT = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        return countS == countT

        # Or we can just use built-in function Counter
        return Counter(s) == Counter(t)