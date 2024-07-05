class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictLetter = {}
        for i in range(ord('a'), ord('z')+1):
            dictLetter[chr(i)] = 0
        for s in text:
            dictLetter[s] += 1
        dictCount = Counter("balloon")
        cnt = float("inf")
        for key, value in dictCount.items():
            cnt = min(cnt, int(dictLetter[key]/value))
        return cnt

        