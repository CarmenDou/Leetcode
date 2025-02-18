class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -int(num))
        result = ""
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        result = str(-heapq.heappop(maxHeap))
        return result
