class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_paths = defaultdict(list)
        blue_paths = defaultdict(list)
        for start, end in redEdges:
            red_paths[start].append(end)
        for start, end in blueEdges:
            blue_paths[start].append(end)

        answer1, answer2 = [-1]*n, [-1]*n
        answer1[0], answer2[0] = 0, 0
        # start from red, 0 means choose red, 1 means choose blue
        q = deque([0])
        step = 0
        visited = set()
        while q:
            tmp = deque([])
            while q:
                node = q.popleft()
                if step%2 == 0:
                    for next_node in red_paths[node]:
                        if (node, next_node, 0) not in visited:
                            visited.add((node, next_node, 0))
                            if answer1[next_node] == -1:
                                answer1[next_node] = step+1
                            tmp.append(next_node)
                else:
                    for next_node in blue_paths[node]:
                        if (node, next_node, 1) not in visited:
                            visited.add((node, next_node, 1))
                            if answer1[next_node] == -1:
                                answer1[next_node] = step+1
                            tmp.append(next_node)

            q = tmp
            step += 1

        # start from blue, 0 means choose blue, 1 means choose red
        q = deque([0])
        step = 0
        visited = set()
        while q:
            tmp = deque([])
            while q:
                node = q.popleft()
                if step%2 == 1:
                    for next_node in red_paths[node]:
                        if (node, next_node, 1) not in visited:
                            visited.add((node, next_node, 1))
                            if answer2[next_node] == -1:
                                answer2[next_node] = step+1
                            tmp.append(next_node)
                else:
                    for next_node in blue_paths[node]:
                        if (node, next_node, 0) not in visited:
                            visited.add((node, next_node, 0))
                            if answer2[next_node] == -1:
                                answer2[next_node] = step+1
                            tmp.append(next_node)

            q = tmp
            step += 1

        answer = [-1]*n
        for i in range(len(answer)):
            if answer1[i] != -1 and answer2[i] != -1:
                answer[i] = min(answer1[i], answer2[i])
            elif answer1[i] != -1 and answer2[i] == -1:
                answer[i] = answer1[i]
            elif answer1[i] == -1 and answer2[i] != -1:
                answer[i] = answer2[i]
        return answer
