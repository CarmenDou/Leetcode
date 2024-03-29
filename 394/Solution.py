# For this question, we need to consdier four conditions.
# If char is a number: we make num+=char.
# If char is '[', we append [num,""].
# If char is a letter, we make stack[-1][1]+=letter(a number is followed by a letter).
# If char is ']', we pop the stack and link the poped string to the former one.
# Lastly we return stack[-1][1].

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        stack = [[1,""]]
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                stack.append([int(num),""])
                num = ""
            elif char == "]":
                n,s = stack.pop()
                stack[-1][1] += n*s
            else:
                stack[-1][1] += char
        return stack[-1][1]
