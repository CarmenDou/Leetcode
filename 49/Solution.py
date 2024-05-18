from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 2
        dic = defaultdict(list)
        for s in strs:
            dic["".join(sorted(s))].append(s)

        return dic.values()

        # Solution 1
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()