from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        sorted_dic = sorted(dic.items(), key = lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            key, value = sorted_dic[i]
            res.append(key)
        return res