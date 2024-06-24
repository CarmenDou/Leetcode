class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # DFS Time Limit Exceeded
        # dictNode = {i: set() for i in range(n)}
        # for e1, e2 in edges:
        #     dictNode[e1].add(e2)
        #     dictNode[e2].add(e1)
        
        # visited = set()
        # self.res = False

        # def dfs(curNode):
        #     if curNode in visited:
        #         return

        #     if curNode == destination:
        #         self.res = True
        #         return

        #     visited.add(curNode)
        #     for node in dictNode[curNode]:
        #         if self.res:  # Early exit if the path has been found
        #             return
        #         dfs(node)
        #     visited.remove(curNode)

        # dfs(source)
        # return self.res

        # BFS
        if source == destination:
            return True
        
        graph = {i: set() for i in range(n)}
        for e1, e2 in edges:
            graph[e1].add(e2)
            graph[e2].add(e1)
        
        visited = set()
        queue = deque([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return False