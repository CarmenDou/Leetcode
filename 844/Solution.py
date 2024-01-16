class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        i,j = 0,0
        while i < len(s):
            if s[i] != "#":
                stack_s.append(s[i])
            else:
                if stack_s:
                    stack_s.pop(-1)
            i += 1 
        while j < len(t):
            if t[j] != "#":
                stack_t.append(t[j])
            else:
                if stack_t:
                    stack_t.pop(-1)
            j += 1
        return (stack_s == stack_t)
        