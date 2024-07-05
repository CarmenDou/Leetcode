class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 1
        maxS = ""
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cnt += 1
            else:
                if cnt >= 3 and num[i-1] > maxS:
                    maxS = num[i-1]
                cnt = 1
        if cnt >= 3 and num[i-1] > maxS:
            maxS = num[i-1]
        return maxS+maxS+maxS
