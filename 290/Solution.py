class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arrWords = s.split()
        if len(pattern) != len(arrWords):
            return False
        dictPattern = {}
        mapWords = set()
        for i in range(len(pattern)):
            if pattern[i] not in dictPattern:
                if arrWords[i] in mapWords:
                    return False
                dictPattern[pattern[i]] = arrWords[i]
                mapWords.add(arrWords[i])
            if dictPattern[pattern[i]] != arrWords[i]:
                return False
        return True
        