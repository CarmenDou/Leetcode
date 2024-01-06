class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for row in range(rowIndex+1):
            temp = []
            if row == 0:
                temp = [1]
                res.append(temp)
            else:
                temp.append(1)
                r = 1
                while r < row:
                    temp.append(res[row-1][r-1]+res[row-1][r])
                    r += 1
                temp.append(1)
                res.append(temp)

        return res[rowIndex]
                    

        
        