class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dictDNA = {}
        res = set()
        for i in range(0, len(s)-9):
            if s[i: i+10] in dictDNA:
                res.add(s[i: i+10])
                dictDNA[s[i: i+10]] += 1
            dictDNA[s[i: i+10]] = 1
        return list(res)