class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        queue, visited = set(), set()
        queue.add("0000")
        visited.add("0000")
        cnt = 0

        while queue:
            if target in visited:
                return cnt
            tmp = set()
            for s in queue:
                for i in range(len(s)):
                    sNew = s[:i] + str((int(s[i])+1)%10) + s[i+1:]
                    if sNew not in visited and sNew not in deadends:
                        visited.add(sNew)
                        tmp.add(sNew)
                    sNew = s[:i] + str((int(s[i])+9)%10) + s[i+1:]
                    if sNew not in visited and sNew not in deadends:
                        visited.add(sNew)
                        tmp.add(sNew)
            queue = tmp
            cnt += 1
        return -1

            
                