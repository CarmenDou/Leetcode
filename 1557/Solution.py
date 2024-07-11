class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        fromCity = {i: [] for i in range(n)}
        toCity = {i: [] for i in range(n)}
        for node1, node2 in edges:
            fromCity[node1].append(node2)
            toCity[node2].append(node1)
        res = []
        for i in range(n):
            if not toCity[i]:
                res.append(i)

        return res
