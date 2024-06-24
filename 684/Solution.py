class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visitedNode = set()
        visitedEdge = set()
        dictEdge = {i: set() for i in range(1, len(edges)+1)}
        for i in range(len(edges)):
            dictEdge[edges[i][0]].add(i)
            dictEdge[edges[i][1]].add(i)

        queue = [0]
        while queue:
            queue.sort()
            i = queue.pop(0)
            visitedEdge.add(i)
            if edges[i][0] in visitedNode and edges[i][1] in visitedNode:
                return edges[i]
            
            if edges[i][0] not in visitedNode:
                visitedNode.add(edges[i][0])
                for edge in dictEdge[edges[i][0]]:
                    if edge not in queue and edge not in visitedEdge:
                        queue.append(edge)
            
            if edges[i][1] not in visitedNode:
                visitedNode.add(edges[i][1])
                for edge in dictEdge[edges[i][1]]:
                    if edge not in queue and edge not in visitedEdge:
                        queue.append(edge)




