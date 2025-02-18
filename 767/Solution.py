class Solution:
    def reorganizeString(self, s: str) -> str:
        count_c = Counter(s)
        maxHeap = [] # pair [num, char]
        for key, value in count_c.items():
           heapq.heappush(maxHeap, [-value, key])
        result = ""
        while len(maxHeap) > 1:
            p1 = heapq.heappop(maxHeap)
            p2 = heapq.heappop(maxHeap)
            result += p1[1] + p2[1]
            if -p1[0]-1 > 0:
                heapq.heappush(maxHeap, [p1[0]+1, p1[1]])
            if -p2[0]-1 > 0:
                heapq.heappush(maxHeap, [p2[0]+1, p2[1]])
        if maxHeap:
            p1 = heapq.heappop(maxHeap)
            if -p1[0] > 1:
                return ""
            result += p1[1]
        return result
