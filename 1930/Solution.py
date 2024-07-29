class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letter = { chr(i) :[] for i in range(ord('a'), ord('z')+1)}
        i, res = 0, 0 
        while i < len(s):
            letter[s[i]].append(i)
            i += 1
        
        def helper(start, end):
            cnt = set()
            i = start+1
            while i < end:
                cnt.add(s[i])
                i += 1
            return len(cnt)
            
        for c, indexList in letter.items():
            if len(indexList) >= 2:
                res += helper(indexList[0], indexList[-1])

        return res