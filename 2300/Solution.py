import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def helper(target):
            l, r = 0, len(potions)-1
            while l <= r:
                mid = (l+r)//2
                if potions[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return len(potions) - mid - 1 if potions[mid] < target else len(potions) - mid
        res = []
        for spell in spells:
            res.append(helper(math.ceil(success/spell)))
        return res