class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
#brute force
#暴力求解
        # res = []
        # for num1 in nums1:
        #     val = -1
        #     index = float('inf')
        #     for key,num2 in enumerate(nums2):
        #         if num1 == num2:
        #             index = key
        #         if key > index and num2 > num1:
        #             val = num2
        #             break
        #     res.append(val)
        # return res
       
# create a monotonically decreasing stack，and use a dictionary to record the next greater element of each num.
# check whether the top element of the stack is greater than current element.
# if so, pop top and record it into dictionary. if not, do nothing.
# pop current element into stack.
# 维护一个单调递减栈，用字典记录下一个最大的数。
# 当前这个数如果比栈顶大，则出栈。
# 再把当前的数压栈
        # stack = []
        # dic = {}
        # for num2 in nums2:
        #     if not stack:
        #         stack.append(num2)
        #     else:
        #         while stack and stack[-1] < num2:
        #             dic[stack[-1]] = num2
        #             stack.pop()
        #         stack.append(num2)
        # while stack:
        #     dic[stack[-1]] = -1
        #     stack.pop()

        # res = []
        # for num1 in nums1:
        #     res.append(dic[num1])
        # return res

# almost the same way like the second way, but we use a list to record the index of the next greater element instead of using dictionary to record the element.
# we can use .index to get the first index of the target num.
# 类似第二种方法，不一样的是用list记录下一个更大数的index，而不是用字典。
# 可以用.index取到目标元素第一次出现的位置
        stack=[]
        next_large=[-1]*len(nums2)
        res=[]
        stack.append(0)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                index=stack.pop()
                next_large[index]=nums2[i]
            stack.append(i)
        
        for num in nums1:
            index=nums2.index(num)
            res.append(next_large[index])
            
        return res
