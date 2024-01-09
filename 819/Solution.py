from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # pattern = r'[^a-z\s]'
        # paragraph = re.sub(pattern," ",paragraph.lower())
        # words = paragraph.split()
        # count = {}
        # for word in words:
        #     if word not in banned:
        #         if word in count:
        #             count[word] += 1
        #         else:
        #             count[word] = 1
        # max_value = -1
        # res = ""
        # for key,value in count.items():
        #     if value > max_value:
        #         res = key
        #         max_value = value

        # return res

        # split the paragraphy by regular expression
        # use package to create dict
        # sort the dict
        # find the first not banned word and return 
        arr_words = re.split("\W+",paragraph.lower())
        dic_words = Counter(arr_words)
        dic_words = sorted(dic_words,key=dic_words.get,reverse=True)
        for word in dic_words:
            if word and word not in banned:
                return word
        return ""
        