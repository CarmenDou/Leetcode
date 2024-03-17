import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in arr:
            for j in arr:
                heapq.heappush(heap, (i/j, i, j))
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        f, i, j = heapq.heappop(heap)
        return [i, j]

import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # heap = []
        # for i in arr:
        #     for j in arr:
        #         heapq.heappush(heap, (i/j, i, j))
        # while k > 1:
        #     heapq.heappop(heap)
        #     k -= 1
        # f, i, j = heapq.heappop(heap)
        # return [i, j]

        nums = arr
        small = 0.0
        large = 1.0
        q = p = 0
        while large - small > 0.0000001:
            mid = small + (large-small)/2
            cnt = 0
            j = 0
            minDiff = 1.0
            for i in range(1, len(nums)):
                while j < i and nums[j]/nums[i] <= mid:
                    if minDiff > mid - nums[j]/nums[i]:
                        minDiff = mid -nums[j]/nums[i]
                        p = nums[i]
                        q = nums[j]
                    j += 1
                cnt += j
            if cnt == k:
                break
            if cnt < k:
                small = mid
            else:
                large = mid
        return (q,p)