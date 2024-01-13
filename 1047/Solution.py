class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # arr = [s[0]]
        # i = 1
        # while i < len(s):
        #     if len(arr) == 0:
        #         arr.append(s[i])
        #     else:
        #         if arr[len(arr)-1] == s[i]:
        #             arr.pop(len(arr)-1)
        #         else:
        #             arr.append(s[i])
        #     i += 1
        # return "".join(arr)

        if not s or len(s) == 1:
            return s
        
        stack = []
        stack.append(s[0])
        
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

1
        