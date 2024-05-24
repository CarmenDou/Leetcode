class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window
        charSet = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

        # myway is use a dic to store last index of this character and when this character appears again, I will know my new substr
        dic_char = {}
        max_count = 0
        sub_str = ""
        for i in range(len(s)):
            char = s[i]
            if char not in sub_str:
                sub_str += char
            else:
                if len(sub_str) > max_count:
                    max_count = len(sub_str)
                sub_str = s[dic_char[char]+1:i+1] 
            dic_char[char] = i
        
        if len(sub_str) > max_count:
            max_count = len(sub_str)
        return max_count

        # Dr.zhang's way is use a pointer i to point the begin index of the sub, and know the new index by poping the character which s[i]!=s[j]
        max_len=1
        if not s:
            return 0
        sub=set(s[0])
        i=0
        for j in range(1,len(s)):
            if s[j] not in sub:
                sub.add(s[j])
            else:
                while s[i]!=s[j]:
                    sub.remove(s[i])
                    i+=1
                i+=1
            max_len=max(max_len,len(sub))
        return max_len

        