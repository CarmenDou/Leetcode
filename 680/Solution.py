# How to judge palindrome From this question, we need to learn how to judge whether one string is palindrome. 
# We can set two pointers, one from left, the other from right. 
# We compare the letter from head with letter from tail. 
# In the case we can delete a letter whatever left or right and check whether it is ok where s[left]!=s[right]. 


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if s == s[::-1]:
        #     return True
        # j = 0
        # while j < len(s):
        #     new_s = s[:j] + s[j+1:]
        #     if new_s == new_s[::-1]:
        #         return True
        #     j += 1
        # return False

        p1=0
        p2=len(s)-1
        while p1<=p2:
            if s[p1]!=s[p2]:
                string1=s[:p1]+s[p1+1:]
                string2=s[:p2]+s[p2+1:]
                return string1==string1[::-1] or string2==string2[::-1]
            p1+=1
            p2-=1
        return True
