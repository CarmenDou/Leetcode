#attention: we should consider the situation when the customer gives you a 20, you should first think about giving a 5 and 10 change to him than giving him 3 5 bills, or you may not have enough 5 bills to change next time.
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        res = True 
        table = {5:0,10:0,20:0}
        for bill in bills:
            if bill == 5:
                table[5] += 1
            elif bill == 10:
                table[10] += 1
                if table[5] > 0 :
                    table[5] -= 1
                else:
                    res = False
                    break
            elif bill == 20:
                table[20] += 1
                if table[10] > 0 and table[5] > 0 and bill <> 0 :
                    table[5] -= 1
                    table[10] -= 1
                    bill = 0
                elif table[5] >=3 and bill <> 0:
                    table[5] -= 3
                    bill = 0
                elif bill <> 0 :
                    res = False
                    break
        return res
        