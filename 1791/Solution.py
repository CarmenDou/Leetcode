from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dicEdges = defaultdict(int)
        for e1, e2 in edges:
            dicEdges[e1] += 1
            dicEdges[e2] += 1
        return sorted(dicEdges.items(), key = lambda x: x[1], reverse = True)[0][0]