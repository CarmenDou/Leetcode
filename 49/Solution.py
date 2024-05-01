from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # res = []
        # aux = []
        # for str in strs:
        #     d = defaultdict(int)
        #     for k in str:
	    #         d[k] += 1
        #     sorted(d.items(),key = lambda x : x[0])
        #     flag = False
        #     for i in range(len(aux)):
        #         if aux[i] == d:
        #             res[i].append(str)
        #             flag = True
        #             break
        #     if not flag:
        #         aux.append(d)
        #         res.append([str])
        # return res

        res = {}
        for word in strs:
            k = "".join(sorted(word))
            if k not in res:
                res[k] = []
            res[k].append(word)
        return (res.values())

        

                
                