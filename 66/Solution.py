class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        res = []
        while num != 0 :
            res.append(num%10)
            num = num / 10
        res.reverse()
        return res
        
# FawneLu
# Firstly, we can convert the list to the string and then to int, then we can make the int plus 1 and convert it back to the list
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=map(str, digits)
        a=str(int("".join(a))+1)
        res=map(int,list(a))
        return res