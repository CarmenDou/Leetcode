class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
        visited, cur = set(), (0, 0)
        visited.add(cur)
        for p in path:
            cur = (cur[0] + directions[p][0], cur[1] + directions[p][1])
            if cur in visited:
                return True
            visited.add(cur)
        return False
