class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(left, right, s):
            if len(s) == n * 2:
                 res.append(s)
                 return 

            if left < n:
                backtrack(left+1, right, s+ '(')

            if right < left:
                backtrack(left,right+1,s +")")

        res = []
        backtrack(0,0,'')
        return res      