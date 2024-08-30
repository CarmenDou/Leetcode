class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = 0
        for p in range(len(bombs)):
            queue = [p]
            visit = []
            visit.append(p)
            while queue:
                m = queue.pop()
                for n in range(len(bombs)):
                    if n not in visit:
                        if (bombs[m][0] - bombs[n][0])**2 + (bombs[m][1] - bombs[n][1])**2 <= bombs[m][2]**2:
                            queue.append(n)
                            visit.append(n)
            res = max(res, len(visit))
        return res 
                    