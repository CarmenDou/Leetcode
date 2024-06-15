class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        prevEnd = [-1]
        i = 0
        while i < len(s):
            tmp = prevEnd
            for j in prevEnd:
                if s[j+1:i+1] in wordDict:
                    tmp.append(i)
                    break
            i += 1
            prevEnd = tmp
        return True if len(s)-1 in prevEnd else False
