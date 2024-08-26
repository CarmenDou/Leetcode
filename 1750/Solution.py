class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif l > 0 and s[l-1] == s[r]:
                r -= 1
            elif r < len(s)-1 and s[l] == s[r+1]:
                l += 1
            else:
                break
        if l == r:
            if (l > 0 and s[l-1] == s[r]) or (r < len(s)-1 and s[l] == s[r+1]):
                return 0
        return r-l+1
        