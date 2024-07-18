class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # res = ""
        # for i in range(1, min(len(str1), len(str2))+1):
        #     tmp1, tmp2 = str1, str2
        #     if tmp1.replace(str1[:i], "") == "" and tmp2.replace(str1[:i], "") == "":
        #         res = str1[:i]
        # return res

        res = ""
        len1, len2 = len(str1), len(str2)
        for i in range(1, min(len1, len2)+1):
            if len1 % i == 0 and len2 % i == 0 and str1[:i]*(int(len1/i)) == str1 and str1[:i]*(int(len2/i)) == str2:
                res = str1[:i]
        return res


