class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        res = []
        products.sort()
        for i in range(len(searchWord)):
            tmp = []
            pre_searchWord = searchWord[:i+1]
            cnt = 0
            for product in products:
                if pre_searchWord == product[:i+1] and cnt < 3:
                    tmp.append(product)
                    cnt += 1
            res.append(tmp)

        return res

        