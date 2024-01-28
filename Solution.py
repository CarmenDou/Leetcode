class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # dic = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        # res = []
        # for digit in digits:
        #     tmp = []
        #     if res:
        #         for r in res:
        #             for q in dic[digit]:
        #                 tmp.append(str(r)+str(q))
        #     else:
        #         for q in dic[digit]:
        #             tmp.append(str(q))
        #     res = tmp
        # return res

        phone = {'2': ['a', 'b', 'c'],'3': ['d', 'e', 'f'],'4': ['g', 'h', 'i'],'5': ['j', 'k', 'l'],'6': ['m', 'n', 'o'],'7': ['p', 'q', 'r', 's'],'8': ['t', 'u', 'v'],'9': ['w', 'x', 'y', 'z']}

        def helper(combination, digits):
            
            if len(digits)==0:
                res.append(combination)
            else:
                for letter in phone[digits[0]]:
                    helper(combination+letter,digits[1:])
        
        res=[]
        if digits:
            helper("",digits)
        return res
                