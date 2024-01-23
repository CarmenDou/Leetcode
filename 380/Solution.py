import random
class RandomizedSet(object):

    def __init__(self):
        self.dic = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.dic[val] = 1
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            del self.dic[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        keys = list(self.dic.keys())
 
        # 从键列表中随机选择一个键
        return random.choice(keys)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()