class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        sorted_p = sorted(p)
        len_s, len_p = len(s), len(p)
        for i in range(0, len_s-len_p+1):
            if sorted(s[i: i+len_p]) == sorted_p:
                res.append(i)
        return res
