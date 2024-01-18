class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operator = ["+","-","*","/"]
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num1-num2)
                elif token == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1/num2))
        return stack[-1]