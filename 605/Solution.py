class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        lenBed = len(flowerbed)
        for i in range(lenBed):
            if flowerbed[i] == 0:
                if i == 0 and ((i+1 < lenBed and flowerbed[i+1] == 0) or i+1 >= lenBed):
                    cnt += 1
                    flowerbed[i] = 1
                elif i == lenBed-1 and ((i-1 >= 0 and flowerbed[i-1] == 0) or i-1 < 0):
                    cnt += 1
                    flowerbed[i] = 1
                elif i > 0 and i < lenBed-1 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    cnt += 1
                    flowerbed[i] = 1
                else:
                    pass
            if cnt >= n:
                return True
        return False