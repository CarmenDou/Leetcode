# Pay attention to how to use deque to create a queue and the function of deque.
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        tmp = deque()
        while len(self.queue) > 1:
            tmp.append(self.queue.popleft())
        res = self.queue.popleft()
        while len(tmp) > 0:
            self.queue.append(tmp.popleft())

        return res

    def top(self) -> int:
        tmp = deque()
        while len(self.queue) > 1:
            tmp.append(self.queue.popleft())
        res = self.queue.popleft()
        tmp.append(res)
        while len(tmp) > 0:
            self.queue.append(tmp.popleft())

        return res

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()