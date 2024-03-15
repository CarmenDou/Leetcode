class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permu = []
        res = []
        visited = [0] * len(nums)
        self.dfs(0, res, nums, visited, permu)
        return res

    def dfs(self, index, res, nums, visited, permu):
        if len(permu) == len(nums):
            res.append(permu) 
            return 
        else:
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    self.dfs(i, res, nums, visited, permu+[nums[i]])
                    print(visited)
                    visited[i] = 0



#         path=[]
#         res=[]
#         visited=[0]*len(nums)
        
#         def backtracking(path):
#             if len(path)==len(nums):
#                 res.append(path)
            
#             for i in range(len(nums)):
#                 if not visited[i]:
#                     visited[i]=1
#                     backtracking(path+[nums[i]])
#                     visited[i]=0
        
#         backtracking(path)
#         return res

        