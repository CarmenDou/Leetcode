class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        if n==0:
            return 0
        low,high=matrix[0][0],matrix[n-1][n-1]
        while low<=high:
            mid=low+(high-low)//2
            print(mid)
            count=0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j]<=mid:
                        count+=1
                    else:
                        break
                    
            if count<k:
                low=mid+1
            else:
                high=mid-1
        
        return low
        