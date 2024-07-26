class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
########20240723 My way################################################
        self.res = []
        candidates.sort()
        def backtrack(i, subset):
            if sum(subset) > target:
                return 
            if sum(subset) == target:
                self.res.append(subset[::])

            for j in range(i, len(candidates)):
                subset.append(candidates[j])
                backtrack(j, subset)
                subset.pop()
        
        backtrack(0, [])
        return self.res


#######################################################################
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res