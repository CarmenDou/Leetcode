class Solution:
    def maxDepth(self, s: str) -> int:
        stack, res = [], 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                stack.pop()
            res = max(res, len(stack))
        return res
