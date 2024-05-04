class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        if fresh == 0:
            return 0

        step = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for direction in directions:
                    dx = direction[0] + x
                    dy = direction[1] + y
                    if dx >= 0 and dy >= 0 and dx < m and dy < n and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        queue.append((dx, dy))
                        fresh -= 1
            step += 1
        
        if fresh != 0:
            return -1
            
        return step-1