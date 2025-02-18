class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            minPath = float('inf')
            for j in range(len(triangle[i])):
                if i != 0:
                    if j == 0:
                        triangle[i][j] += triangle[i-1][j]
                    elif j > 0 and j < len(triangle[i])-1:
                        triangle[i][j] = min(triangle[i][j]+triangle[i-1][j-1], triangle[i][j]+triangle[i-1][j])
                    else:
                        triangle[i][j] += triangle[i-1][j-1]
                minPath = min(minPath, triangle[i][j])
            # print(triangle[i])
        return minPath

