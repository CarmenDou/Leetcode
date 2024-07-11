from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        fromCity = defaultdict(list)
        toCity = defaultdict(list)
        for connection in connections:
            fromCity[connection[0]].append(connection[1])
            toCity[connection[1]].append(connection[0])
        
        queue, cnt = [0], 0
        while queue:
            node = queue.pop()
            visited.add(node)
            if node in toCity:
                for city in toCity[node]:
                    if city not in visited:
                        queue.append(city)
            if node in fromCity:
                for city in fromCity[node]:
                    if city not in visited:
                        queue.append(city)
                        cnt += 1
        return cnt