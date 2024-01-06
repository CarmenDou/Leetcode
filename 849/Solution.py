# Luqi's way: first we can count the number of zero in the head and tail of the list, and then we can count the maximum number of continuous zero in the list.
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res=0
        count=0
        left=0
        right=len(seats)-1
        count_left=0
        count_right=0
        while seats[left]==0:
            count_left+=1
            left+=1
        while seats[right]==0:
            count_right+=1
            right-=1
        count_zero=max(count_right,count_left)
        
        for i in range(len(seats)):
            if seats[i]==0:
                count+=1
                res=max(count,res)
            if seats[i]==1:
                count=0
                
            
        return max((res+1)//2,count_zero)

# My way: It is similar but not that clear, because I dont know how to process the head and tail of the list clearly. 
# import math
# class Solution(object):
#     def maxDistToClosest(self, seats):
#         """
#         :type seats: List[int]
#         :rtype: int
#         """
#         maxDistance = 0
#         lIndex = -1
#         Distance = 0
#         for i in range(len(seats)) :
#             if seats[i] == 1 :
#                 if lIndex == -1 :
#                     maxDistance = i
#                 else :
#                     Distance = int(math.floor((i-lIndex)/2))
#                 lIndex = i    
#                 if maxDistance < Distance :
#                     maxDistance = Distance
#                 Distance = 0
#             else :
#                 Distance += 1
        
#         if maxDistance < Distance :
#            maxDistance = Distance

#         return maxDistance

