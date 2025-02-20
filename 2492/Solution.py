from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dict_roads = defaultdict(list)
        for node1, node2, distance in roads:
            dict_roads[node1].append((node2, distance))
            dict_roads[node2].append((node1, distance))


        # DFS
        # def dfs(i):
        #     if i in visit:
        #         return
        #     visit.add(i)
        #     nonlocal res
        #     for nei, dist in dict_roads[i]:
        #         res = min(res, dist)
        #         dfs(nei)

        # res = float("inf")
        # visit = set()
        # dfs(1)
        # return res

        q = deque([1])
        min_distance = float("inf")
        visited = set()
        visited.add(1)
        while q:
            node = q.popleft()
            for nei, dist in dict_roads[node]:
                min_distance = min(min_distance, dist)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return min_distance