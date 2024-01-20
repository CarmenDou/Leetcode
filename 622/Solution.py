class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.circular_queue = [-1]*(k+1)
        self.front = 0
        self.rear = 0
        self.size = k+1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.circular_queue[self.rear] = value
            self.rear = (self.rear+1)%self.size
            return True
        else:
            return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.circular_queue[self.front] = None
            self.front = (self.front+1)%self.size
            return True
        else:
            return False
        

    def Front(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.circular_queue[self.front]
        else:
            return -1
        

    def Rear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.circular_queue[self.rear-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if (self.rear+1)%self.size == self.front:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()