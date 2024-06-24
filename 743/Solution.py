class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dictEdge = {i: [] for i in range(1, n+1)}
        # visitedEdge = set()
        # visitedNode = set()
        # minTime = [0] * (n+1)
        # for source, target, weight in times:
        #     dictEdge[source].append([source, target, weight])

        # visitedNode.add(k)
        # while True:
        #     queue = []
        #     for node in visitedNode:
        #         for edge in dictEdge[node]:
        #             if edge[1] not in visitedNode:
        #                 queue.append([edge[0], edge[1],edge[2]+minTime[edge[0]]])
        #     if not queue:
        #         break
        #     queue.sort(key=lambda x : x[2])
        #     source, destination, weight = queue[0][0], queue[0][1],queue[0][2]
        #     minTime[destination] = weight
        #     visitedNode.add(destination)

        # if len(visitedNode) == n:
        #     return max(minTime)
        # else:
        #     return -1

        graph=collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))
        
        dist={node: float('inf') for node in range(1,n+1)}
        
        def dfs(node,time):
            if time>=dist[node]:
                return 
            dist[node]=time
            for t, n in sorted(graph[node]):
                dfs(n,time+t)
                
        dfs(k,0)
        res=max(dist.values())
        return res if res<float('inf') else -1


