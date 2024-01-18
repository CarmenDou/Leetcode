# My way, set a variable move to record the result.
# If we meet the ( then append.
# If we meet the ) then
#  1) If stack[-1] is the (, then we can pop stack[-1]
#  2) If not, move add 1
# In the end, move add the remain element in the stack and return move.
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        move = 0
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    move += 1
        return move+len(stack)

        return move

# For this question, we need to kwnoe that how many invalid parentheses left in the string.
# If we meet the (, then append it in the stack.
# If we weet the ), then we decide whether the last parentheses is (.
#  1) If so, it proves that the new parenthese has its pair, the we pop that last one.
#  2) If not, we append the ) in the stack.

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for s in S:
            if s=='(':
                stack.append(s)
            else:
                if stack!=[] and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(s)
        return len(stack)
        