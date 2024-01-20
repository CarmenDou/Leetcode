# implement deque by myself instead of using built-in function.
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k+1
        self.deque = [-1] * self.size
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.head = (self.head-1+self.size)%self.size
            self.deque[self.head] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque[self.tail] = value
            self.tail = (self.tail+1)%self.size
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque[self.head] = None
            self.head = (self.head+1)%self.size
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque[self.tail] = None
            self.tail = (self.tail-1+self.size)%self.size
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.head]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[self.tail-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return True if self.head == self.tail else False

    def isFull(self) -> bool:
        return True if (self.tail+1)%self.size == self.head else False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = deque()
        self.size = k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.deque.appendleft(value)
            return True
        else:
            return False
        
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.deque.append(value)
            return True
        else:
            return False
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.deque.popleft()
            return True
        else:
            return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.deque.pop()
            return True
        else:
            return False
        

    def getFront(self):
        """
        :rtype: int
        """
        return self.deque[0] if self.deque else -1
        

    def getRear(self):
        """
        :rtype: int
        """
        return self.deque[-1] if self.deque else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return True if not self.deque else False

    def isFull(self):
        """
        :rtype: bool
        """
        return True if len(self.deque) == self.size else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()