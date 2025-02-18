class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # count = defaultdict(int)
        # for n in arr:
        #     count[n] += 1
        # sorted_count = sorted(count.values())
        # result = len(sorted_count)
        # for i in range(len(sorted_count)):
        #     if k > 0:
        #         k -= sorted_count[i]
        #         if k >= 0:
        #             result -= 1
        # return result

        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)

        res = len(heap)
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
        return res