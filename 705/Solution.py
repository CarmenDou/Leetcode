class MyHashSet(object):

#     def __init__(self):
#         self.hashset = set()

#     def add(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         self.hashset.add(key)
        

#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         if key in self.hashset:
#             self.hashset.remove(key)
        

#     def contains(self, key):
#         """
#         :type key: int
#         :rtype: bool
#         """
#         return True if key in self.hashset else False
        


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.keyRange = 769
    #     self.bucketArray = [set() for i in range(self.keyRange)]

    # def _hash(self, key):
    #     return key % self.keyRange

    # def add(self, key):
    #     """
    #     :type key: int
    #     :rtype: None
    #     """
    #     bucketIndex = self._hash(key)
    #     self.bucketArray[bucketIndex].add(key)

    # def remove(self, key):
    #     """
    #     :type key: int
    #     :rtype: None
    #     """
    #     bucketIndex = self._hash(key)
    #     if self.contains(key):
    #         self.bucketArray[bucketIndex].remove(key)

    # def contains(self, key):
    #     """
    #     Returns true if this set contains the specified element
    #     :type key: int
    #     :rtype: bool
    #     """
    #     bucketIndex = self._hash(key)
    #     return True if key in self.bucketArray[bucketIndex] else False

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False