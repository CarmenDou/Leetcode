class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        transposeMatrix = [[-1 for i in range(m)] for j in range(n)]
        #print(transposeMatrix)
        for i in range(m) :
            for j in range(n) :
                transposeMatrix[j][i] = matrix[i][j]
        return transposeMatrix