class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while num > 0:
            if num % 2 == 0:
                num = num/2
            else:
                num = num - 1
            step += 1
        return step
        

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        if num == 0:
            return count
        while num:
            if num & 1:
                count+=2
            else:
                count+=1
            num=num>>1
        return count-1