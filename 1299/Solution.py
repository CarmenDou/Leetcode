class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        for i in range(len(arr)-2, -1, -1):
            res[i] = max(res[i+1], arr[i+1])
        return res