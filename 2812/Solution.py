class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # thiefs = []
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c]:
        #             thiefs.append((r, c))

        # def cal_min_distance(r, c):
        #     min_distance = float('inf')
        #     for r_t, c_t in thiefs:
        #         min_distance = min(min_distance, abs(r-r_t)+abs(c-c_t))
        #     return min_distance

        # h = []
        # heapq.heapify(h)
        # result = float('inf')
        # heapq.heappush(h, (-cal_min_distance(0, 0), (0, 0)))
        # visited = set()
        # caled = set()
        # while h:
        #     # print(h)
        #     min_distance, (r, c) = heapq.heappop(h)
        #     if (r, c) in visited:
        #         continue

        #     result = min(result, -min_distance)
        #     if result == 0 or (r, c) == (ROWS-1, COLS-1):
        #         return result

        #     visited.add((r, c))
        #     for dr, dc in directions:
        #         if r+dr >= 0 and r+dr < ROWS and c+dc >= 0 and c+dc < COLS and (r+dr, c+dc) not in visited and (r+dr, c+dc) not in caled:
        #             # temp_distance = -cal_min_distance(r+dr, c+dc)
        #             # if (-cal_min_distance(r+dr, c+dc), (r+dr, c+dc)) not in h:
        #             heapq.heappush(h, (-cal_min_distance(r+dr, c+dc), (r+dr, c+dc)))

        # return 0
            

        N = len(grid)

        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        def precompute():
            q = deque()
            min_dist = {}
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            while q:
                r, c, dist = q.popleft()
                nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for r2, c2 in nei:
                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist+1
                        q.append([r2, c2, dist+1])
            return min_dist

        min_dist = precompute()
        maxHeap = [(-min_dist[(0, 0)], 0, 0)]
        visit = set()
        visit.add((0, 0))
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist
            if (r, c) == (N-1, N-1):
                return dist

            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for r2, c2 in nei:
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(maxHeap, (-dist2, r2, c2))

