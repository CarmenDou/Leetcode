class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j :
            if numbers[i] + numbers[j] > target :
                j -= 1
            elif numbers[i] + numbers[j] < target :
                i += 1
            elif numbers[i] + numbers[j] == target :
                return [i+1, j+1]


# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(numbers)) :
#             for j in range(len(numbers)) :
#                 if numbers[i] + numbers[j] == target :
#                     return [i+1,j+1]
        
        