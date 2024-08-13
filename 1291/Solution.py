class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        base = "123456789"
        nums = []
        i, j = 0, 0
        for i in range(len(base)):
            for j in range(len(base)-i):
                nums.append(int(base[j:j+i+1]))
        res = []
        for num in nums:
            if num >= low and num <= high:
                res.append(num)
        return res