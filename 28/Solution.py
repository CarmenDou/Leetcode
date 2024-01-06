class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while i < len(haystack) - len(needle) + 1 :
            if haystack[i:i+len(needle)] == needle :
                return i
            i += 1
        return -1
        
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         i = 0
#         while i < len(haystack) :
#             p = i
#             q = 0
#             while p < len(haystack) and q < len(needle) :
#                 if haystack[p] != needle[q] :
#                     break
#                 p += 1
#                 q += 1
#             if q == len(needle) :
#                 return i
#             i += 1
#         return -1

        