class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        structure = defaultdict(list)
        for e, h in enumerate(manager):
            structure[h].append(e)

        self.maxTime = 0

        def helper(hid, totalTime):
            if hid not in structure:
                self.maxTime = max(self.maxTime, totalTime)
                return

            for e in structure[hid]:
                totalTime += informTime[hid]
                helper(e, totalTime)
                totalTime -= informTime[hid]
        
        helper(headID, 0)
        return self.maxTime
