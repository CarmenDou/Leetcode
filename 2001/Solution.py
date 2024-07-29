class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dictRectangles = {}

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        for i in range(len(rectangles)):
            w, h = rectangles[i][0], rectangles[i][1]
            i = gcd(w, h)
            if (w/i, h/i) not in dictRectangles:
                dictRectangles[(w/i, h/i)] = []
            dictRectangles[(w/i, h/i)].append(i)
        
        res = 0
        for key, value in dictRectangles.items():
            res += len(value) * (len(value)-1) / 2
        return int(res)