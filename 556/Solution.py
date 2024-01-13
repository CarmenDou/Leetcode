class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # str_n = str(n)
        # str1 = ""
        # str2 = ""
        # res = "-1"
        # for i in range(len(str_n)-1,0,-1):
        #     print(i)
        #     print(str_n[i-1])
        #     print(str_n[i])
        #     if str_n[i-1] < str_n[i]:
        #         str1 = str_n[:i-1]
        #         str2 = str_n[i:][::-1]
        #         for j in range(len(str2)):
        #             if str_n[i-1] < str2[j]:
        #                 res = str1 + str2[j] + str2[:j] + str_n[i-1] + str2[j+1:]
        #                 break
        #         break
        # res = int(res,10)
        # if res >= 2147483648:
        #     return -1
        # return res

#反转string，先找到从后向前数，第一个降序的位置，把此位置后面的翻转。再把这个降序数字和后面第一个比它大的位置交换即可。
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n=list(str(n))
        i=len(n)-1
        while i>0 and n[i-1]>=n[i]:
            i-=1
        if i==0:
            return -1
        self.reverse(n,i,len(n)-1)
        #print(n,i)
        for j in range(i,len(n)):
            if n[j]>n[i-1]:
                self.swap(n,j,i-1)
                break
        res = int("".join(n))
        return res if res<2**31 else -1
        
    
    def reverse(self,nums,i,j):
        for k in range(i,(i+j)//2+1):
            self.swap(nums,k,i+j-k)
        
    
    def swap(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]
