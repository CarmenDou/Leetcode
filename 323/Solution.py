class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit_nodes = set()
        visit_edges = [False]*len(edges)
        res = 0

        def dfs(i):
            visit_nodes.add(i)
            for j in range(len(edges)):
                if not visit_edges[j] and i in edges[j]:
                    visit_edges[j] = True
                    if edges[j][0] != i:
                        dfs(edges[j][0])
                    else:
                        dfs(edges[j][1])


        for i in range(n):
            if i not in visit_nodes:
                res += 1
                dfs(i)
        
        return res

