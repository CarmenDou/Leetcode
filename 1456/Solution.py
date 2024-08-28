class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, curVowel, res = 0, 0, 0
        while i < k-1:
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                curVowel += 1
            i += 1
        while i < len(s):
            if i-k >= 0:
                if s[i-k] in ['a', 'e', 'i', 'o', 'u']:
                    curVowel -= 1
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                    curVowel += 1
            i += 1
            res = max(res, curVowel)
        return res
            
