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