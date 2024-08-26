class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i, cnt, res = 0, 0, 0
        while i < k-1:
            cnt += arr[i]
            i += 1
        while i < len(arr):
            if i - k < 0:
                cnt = cnt + arr[i]
            else:
                cnt = cnt + arr[i] - arr[i-k]
            if cnt >= threshold * k:
                res += 1
            i += 1
        return res
