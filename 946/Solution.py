# For this question, we need to come up with one thing that whether the element in the stack is the same with the popped's top element.
# We append pushed's first element in the stack.
# If the top element in the stack is the same with fisrt element in the popped, then we pop stack and stack.
# For lower time complexity, we need to reverse pushed and popped. We also use pushed==[] to as the termination maker.
# 这道题，我们每次都判断stack的最后一个元素是否跟popped的第一个元素相等。如果相等，两个同时出栈。如果不等，我们把pushed元素按顺序压入栈中。 为了减少时间复杂度，我们可以先反转pushed和popped两个list。

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
# My way is easy to be confused.

        # stack = []
        # while pushed or popped:
        #     if not stack and pushed:
        #         stack.append(pushed.pop(0))
        #     else:
        #         if popped[0] == stack[-1]:
        #             stack.pop(-1)
        #             popped.pop(0)
        #         elif pushed:
        #             stack.append(pushed.pop(0))
        #         else:
        #             break
        # return (not stack)

# using pop is a little time-consuming, we can use index replacing really operations.
# But, better way is to reverse the list.
        # stack = []
        # i = 0
        # j = 0
        # while i < len(pushed) or j < len(popped):
        #     if not stack and i < len(pushed):
        #         stack.append(pushed[i])
        #         i += 1
        #     else:
        #         if popped[j] == stack[-1]:
        #             stack.pop(-1)
        #             j += 1
        #         elif i < len(pushed):
        #             stack.append(pushed[i])
        #             i += 1
        #         else:
        #             break
        # return (not stack)

# Better way
# For this question, we need to come up with one thing that whether the element in the stack is the same with the popped's top element.
# We append pushed's first element in the stack.
# If the top element in the stack is the same with fisrt element in the popped, then we pop stack and stack.
# For lower time complexity, we need to reverse pushed and popped. We also use pushed==[] to as the termination maker.
# 这道题，我们每次都判断stack的最后一个元素是否跟popped的第一个元素相等。如果相等，两个同时出栈。如果不等，我们把pushed元素按顺序压入栈中。 为了减少时间复杂度，我们可以先反转pushed和popped两个list。
        stack = []
        pushed = pushed[::-1]
        popped = popped[::-1]
        while True:
            stack.append(pushed.pop())
            while stack and stack[-1] == popped[-1]:
                stack.pop(-1)
                popped.pop()

            if not pushed:
                break
        
        return (not stack)
