class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        stack = stack[:len(stack)- k]
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        return "".join(stack[i:]) if "".join(stack[i:]) else "0"