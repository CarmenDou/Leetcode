class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []

        for i in s:
            if i.isdigit():
                num = num*10 +int(i)

            if i in "+-":
                res += num * sign
                num = 0
                sign = 1 if i == "+" else  -1

            if i == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            if i == ")":
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num = 0

        res += num*sign

        return res

            
        
        