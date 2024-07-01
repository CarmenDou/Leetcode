class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicIso = {}
        visited = set()
        for i in range(len(s)):
            if s[i] not in dicIso:
                if t[i] in visited:
                    return False
                dicIso[s[i]] = t[i]
                visited.add(t[i])
            else:
                if dicIso[s[i]] != t[i]:
                    return False
        return True