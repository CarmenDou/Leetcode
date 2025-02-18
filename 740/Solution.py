class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_num = Counter(nums)
        count_num = list(count_num.items())
        count_num.sort(key = lambda x: x[0]) # num, count
        dp = [[0, 0]]*len(count_num) #include, not include
        dp[0] = [count_num[0][0] * count_num[0][1], 0]
        for i in range(1, len(count_num)):
            if count_num[i-1][0]+1 == count_num[i][0]:
                include = count_num[i][0]*count_num[i][1] + dp[i-1][1]
            else:
                include = max(dp[i-1][0], dp[i-1][1]) + count_num[i][0]*count_num[i][1]
            not_include = max(dp[i-1][0], dp[i-1][1])
            dp[i] = [include, not_include]
        return max(dp[len(count_num)-1][0], dp[len(count_num)-1][1])