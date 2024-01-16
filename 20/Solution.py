class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        i = 0
        while i < len(s):
            if not stack:
                stack.append(s[i])
            else:
                if (stack[-1] == "(" and s[i] == ")") or (stack[-1] == "[" and s[i] == "]") or (stack[-1] == "{" and s[i] == "}"):
                    stack.pop(-1)
                else:
                    stack.append(s[i])
            i += 1
        return (not stack)