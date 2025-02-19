from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        ### DFS
        # dict_edges = defaultdict(list)
        # dict_succProb = defaultdict(int)
        # for i, [node1, node2] in enumerate(edges):
        #     dict_edges[node1].append(node2)
        #     dict_succProb[(node1, node2)] = succProb[i]
        #     dict_edges[node2].append(node1)
        #     dict_succProb[(node2, node1)] = succProb[i]
        # # print(dict_succProb)
        # self.maxPro = 0
        # def dfs(curNode, curPro, visited):
        #     if curNode == end_node:
        #         self.maxPro = max(self.maxPro, curPro)

        #     visited.add(curNode)
        #     for node in dict_edges[curNode]:
        #         if node not in visited:
        #             # print(curNode, node)
        #             # curPro = curPro * dict_succProb[(curNode, node)]
        #             # print(curPro)
        #             dfs(node, curPro * dict_succProb[(curNode, node)], visited)
        #             # print(curPro)
        #             # curPro = curPro / dict_succProb[(curNode, node)]
        #     visited.remove(curNode)

        # dfs(start_node, 1, set())
        # return self.maxPro

        ### BFS
        dict_edges = defaultdict(list)
        dict_succProb = defaultdict(int)
        for i, [node1, node2] in enumerate(edges):
            dict_edges[node1].append(node2)
            dict_succProb[(node1, node2)] = succProb[i]
            dict_edges[node2].append(node1)
            dict_succProb[(node2, node1)] = succProb[i]
        h = [(-1, start_node)]
        heapq.heapify(h)
        visited = set()
        while h:
            # print(h)
            cur_prob, cur_node = heapq.heappop(h)
            if cur_node == end_node:
                return -cur_prob
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for node in dict_edges[cur_node]:
                heapq.heappush(h, (cur_prob * dict_succProb[(cur_node, node)], node))
        return 0

        