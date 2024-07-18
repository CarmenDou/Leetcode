class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, curCandidate):
            if sum(curCandidate) == target:
                res.append(curCandidate[::])
                return 
            if i >= len(candidates) or sum(curCandidate) > target:
                return
            
            curCandidate.append(candidates[i])
            backtrack(i+1, curCandidate)
            curCandidate.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curCandidate)
        
        backtrack(0, [])
        return res