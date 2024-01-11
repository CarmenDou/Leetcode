class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        sym = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        sorted_sym = sorted(sym.items(), key=lambda x: x[1], reverse=True)
        if num != 0:
            for key,value in sorted_sym:
                count = num//value
                if count != 0:
                    num = num - count*value
                    while count > 0:
                        res = res + key
                        count -= 1

        return res