from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        sort_dic = sorted(dic.items(),key = lambda x : (-x[1],x[0]))[:k]
        return [ string for string, count in sort_dic]      
        