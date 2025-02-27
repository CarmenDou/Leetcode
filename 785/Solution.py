class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        node = [0]*len(graph) #0 means, not visited, 1 means belong to set A, 2 means belong to set B
        visited = set()
        self.flag = True
        def dfs(i):
            for j in graph[i]:
                if node[j] == node[i]:
                    self.flag = False
                else:
                    if node[i] == 1:
                        node[j] = 2
                    else:
                        node[j] = 1
                if (i, j) not in visited:
                    visited.add((i, j))
                    visited.add((j, i))
                    dfs(j)


        for i in range(len(node)):
            if not node[i]:
                node[i] = 1
                dfs(i)
                if not self.flag:
                    return False
        return True
