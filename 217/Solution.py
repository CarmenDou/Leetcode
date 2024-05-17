from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # My Solution
        if not nums:
            return False
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for key, value in dic.items():
            if value > 1:
                return True
        return False

        # Solution3
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

        #Solution2
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False