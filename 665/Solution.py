class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nonDec = []
        tmp = []
        for num in nums:
            if tmp:
                if tmp[-1] > num:
                    nonDec.append(tmp)
                    tmp = []
            tmp.append(num)
        nonDec.append(tmp)
        if len(nonDec) < 2:
            return True
        elif len(nonDec) == 2:
            l1, l2 = nonDec[0], nonDec[1]
            if len(l1) < 2 or (len(l1) >= 2 and l1[-2] <= l2[0]):
                return True
            if len(l2) < 2 or (len(l2) >= 2 and l1[-1] <= l2[1]):
                return True
            return False
        else:
            return False