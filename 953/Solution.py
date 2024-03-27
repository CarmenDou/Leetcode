class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        while len(words) > 1:
            word1 = list(words[0])
            word2 = list(words[1])
            iFlag = False
            while word1 and word2:
                w1 = word1.pop(0)
                w2 = word2.pop(0)
                if order.index(w1) < order.index(w2):
                    iFlag = True
                    break
                elif order.index(w1) > order.index(w2):
                    return False
            if not iFlag and word1 and not word2:
                return False

            words.pop(0)

        return True
                

        