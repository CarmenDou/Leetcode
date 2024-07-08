class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dictCnt = {}
        longest = -1
        for i in range(len(s)):
            if s[i] in dictCnt:
                longest = max(longest, i-dictCnt[s[i]]-1)
            else:
                dictCnt[s[i]] = i
        return longest