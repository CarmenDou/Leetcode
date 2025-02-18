class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dictCount = Counter(nums)
        sorted_dictCount = sorted(dictCount.items(), key = lambda x: x[1], reverse = True)
        result = [[] for r in range(sorted_dictCount[0][1])]
        for value, cnt in sorted_dictCount:
            for r in range(cnt):
                result[r].append(value)
        return result