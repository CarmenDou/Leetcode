from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distances = [[float("inf") for i in range(len(edges))] for j in range(2)]
        distances[0][node1] = 0
        distances[1][node2] = 0
        q = deque([node1])
        visited = set()
        step = 0
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                next_node = edges[node]
                if next_node != -1 and next_node not in visited:
                    step += 1
                    distances[0][next_node] = step
                    q.append(next_node)

        q = deque([node2])
        visited = set()
        step = 0
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                next_node = edges[node]
                if next_node != -1 and next_node not in visited:
                    step += 1
                    distances[1][next_node] = step
                    q.append(next_node)
            
        min_index = float("inf")
        min_distance = float("inf")
        for i in range(len(edges)):
            tmp = max(distances[0][i], distances[1][i])
            if tmp < min_distance:
                min_distance = tmp
                min_index = i
            elif tmp == min_distance and min_distance != float("inf"):
                min_index = min(min_index, i)

        return min_index if min_index != float("inf") else -1