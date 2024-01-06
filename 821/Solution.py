class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = []
        strList = list(s)
        for x in range(len(strList)) :
            minD = len(strList)
            for y in range(len(strList)) :
                if strList[y] == c and abs(x - y) < minD :
                    minD = abs(x - y)
            res.append(minD)
        return res

#Leetcode
#we can convert the question into find the min distance between the two below :
#the closest str C before s[i]
#the closest str C after s[i]

# 问题可以转换成，对 s 的每个下标 i，求
# s[i] 到其左侧最近的字符 c 的距离
# s[i] 到其右侧最近的字符 c 的距离
# 这两者的最小值。

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res=[0] * n
        index = -n
        for i,ch in enumerate(S) :
            if ch == C :
                index = i
            res[i] = i - index

        index = 2 * n
        for i in range(n-1,-1,-1) :
            if S[i] == C :
                index = i
            res[i] = min(res[i],index-i)      
        return res